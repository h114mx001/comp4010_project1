import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Load and process data
def load_data():
    # Load datasets
    gii_df = pd.read_csv('support_datasets/Gender Inequality Index.csv')
    results_df = pd.read_csv('datasets/country_results_df.csv')
    
    # Melt GII data to convert years to rows
    gii_melted = gii_df.melt(
        id_vars=['Country', 'Continent', 'Human Development Groups'],
        value_vars=[col for col in gii_df.columns if 'Gender Inequality Index' in col],
        var_name='Year',
        value_name='GII'
    )
    # Extract year from column name
    gii_melted['Year'] = gii_melted['Year'].str.extract('(\d{4})').astype(int)
    
    # Process results data
    results_df['year'] = pd.to_numeric(results_df['year'])
    results_df['team_size_female'] = pd.to_numeric(results_df['team_size_female'])
    results_df['team_size_all'] = pd.to_numeric(results_df['team_size_all'])
    results_df['female_ratio'] = results_df['team_size_female'] / results_df['team_size_all']
    
    # Calculate total medals
    medal_cols = ['awards_gold', 'awards_silver', 'awards_bronze']
    for col in medal_cols:
        results_df[col] = pd.to_numeric(results_df[col], errors='coerce').fillna(0)
    results_df['total_medals'] = results_df[medal_cols].sum(axis=1)
    
    # Merge datasets
    merged_df = pd.merge(
        results_df,
        gii_melted,
        left_on=['country', 'year'],
        right_on=['Country', 'Year'],
        how='inner'
    )
    
    development_order = ['Very High', 'High', 'Medium', 'Low']
    merged_df['Human Development Groups'] = pd.Categorical(
        merged_df['Human Development Groups'],
        categories=development_order,
        ordered=True
    )
    
    return merged_df

# Initialize Dash app
app = dash.Dash(__name__)

# Load data
df = load_data()

# App layout
app.layout = html.Div([
    html.H1("Gender Inequality Index and IMO Performance Analysis"),
    
    html.Div([
        html.Label("Select Visualization:"),
            dcc.Dropdown(
            id='viz-type',
            options=[
                {'label': 'Female Participation Trend', 'value': 'female_trend'},
                {'label': 'Female Participation by Continent', 'value': 'continent_trend'},
                {'label': 'GII Trend by Development Group', 'value': 'gii_trend'},
                {'label': 'Gender Distribution Over Time', 'value': 'gender_trend'}  # Add this option
            ],
            value='gii_medals'
            )
    ]),
    
    html.Div([
        dcc.Graph(id='main-graph')
    ])
])

# Callback to update graph
@app.callback(
    Output('main-graph', 'figure'),
    [Input('viz-type', 'value')]
)
def update_graph(viz_type):  
    if viz_type == 'female_trend':
        # Calculate average female ratio by year and development group
        yearly_avg = df.groupby(['Year', 'Human Development Groups'])['female_ratio'].mean().reset_index()
        
        fig = px.line(
            yearly_avg,
            x='Year',
            y='female_ratio',
            color='Human Development Groups',
            title='Female Participation Trend by Development Group'
        )
    elif viz_type == 'gender_trend':
        # Load timeline data
        timeline_df = pd.read_csv('datasets/timeline_df.csv')
        
        # Create figure with secondary y-axis
        fig = go.Figure()
        
        # Add traces for male and female contestants
        fig.add_trace(
            go.Scatter(
                x=timeline_df['year'],
                y=timeline_df['male_contestant'],
                name='Male Contestants',
                line=dict(color='#2980b9', width=2)
            )
        )
        
        fig.add_trace(
            go.Scatter(
                x=timeline_df['year'],
                y=timeline_df['female_contestant'],
                name='Female Contestants',
                line=dict(color='#e74c3c', width=2)
            )
        )
        
        # Update layout
        fig.update_layout(
            title='Gender Distribution in IMO Contestants (1959-2024)',
            xaxis_title='Year',
            yaxis_title='Number of Contestants',
            hovermode='x unified',
            plot_bgcolor='rgba(240,240,240,0.2)',
            paper_bgcolor='white',
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01
            )
        )
        
        # Add range slider
        fig.update_xaxes(rangeslider_visible=True)
    elif viz_type == 'continent_trend':
        # Add new visualization for continent-based analysis
        yearly_continent = df.groupby(['Year', 'Continent']).agg({
            'female_ratio': 'mean',
            'GII': 'mean',
            'total_medals': 'sum'
        }).reset_index()
        
        fig = px.line(
            yearly_continent,
            x='Year',
            y='female_ratio',
            color='Continent',
            title='Female Participation Trend by Continent',
            labels={'female_ratio': 'Female Participation Ratio'},
            hover_data=['total_medals', 'GII']
        )
        
        # Add range slider for better time navigation
        fig.update_xaxes(rangeslider_visible=True)
    else:  # gii_trend
        # Calculate average GII by year and development group
        yearly_gii = df.groupby(['Year', 'Human Development Groups'])['GII'].mean().reset_index()
        
        fig = px.line(
            yearly_gii,
            x='Year',
            y='GII',
            color='Human Development Groups',
            title='Gender Inequality Index Trend by Development Group'
        )
    
    fig.update_layout(
        xaxis_title=fig.layout.xaxis.title.text,
        yaxis_title=fig.layout.yaxis.title.text,
        legend_title="Human Development Groups"
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)