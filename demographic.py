import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots  # Add this line

# Initialize the Dash app
app = dash.Dash(__name__)

# Load and process data
def load_data():
    results_df = pd.read_csv('datasets/country_results_df.csv')
    gdp_df = pd.read_csv('support_datasets/GDP.csv')
    
    # Melt GDP data to convert years from columns to rows
    gdp_melted = gdp_df.melt(
        id_vars=['Country', 'Country Code'],
        value_vars=[str(year) for year in range(1960, 2023)],
        var_name='year',
        value_name='GDP'
    )
    gdp_melted['year'] = pd.to_numeric(gdp_melted['year'])
    
    # Prepare results data
    results_df['year'] = pd.to_numeric(results_df['year'])
    medal_cols = ['awards_gold', 'awards_silver', 'awards_bronze']
    for col in medal_cols:
        results_df[col] = pd.to_numeric(results_df[col], errors='coerce').fillna(0)
    results_df['total_medals'] = results_df[medal_cols].sum(axis=1)
    
    # Merge datasets
    merged_df = pd.merge(
        results_df[['country', 'year', 'total_medals']], 
        gdp_melted[['Country', 'year', 'GDP']],
        left_on=['country', 'year'],
        right_on=['Country', 'year'],
        how='inner'
    )
    
    merged_df['GDP'] = pd.to_numeric(merged_df['GDP'], errors='coerce')
    merged_df.dropna(subset=['GDP'], inplace=True)
    
    return merged_df

# Load the data
df = load_data()

# Custom CSS styling
app.layout = html.Div([
    # Header section
    html.Div([
        html.H1("GDP vs Olympic Medals Analysis (1960-2022)", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 30}),
        html.P("Explore the relationship between country GDP and Olympic performance over time", 
               style={'textAlign': 'center', 'color': '#7f8c8d'})
    ], style={'marginBottom': 40}),
    
    # Controls section
    html.Div([
        # Year selector
        html.Div([
            html.Label("Select Year:", style={'fontWeight': 'bold', 'color': '#2c3e50'}),
            dcc.Slider(
                id='year-slider',
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].max(),
                marks={str(year): str(year) for year in df['year'].unique()},
                step=None
            )
        ], style={'width': '100%', 'marginBottom': 30}),
        
        # Country selector
        html.Div([
            html.Label("Select Country:", style={'fontWeight': 'bold', 'color': '#2c3e50'}),
            dcc.Dropdown(
                id='country-dropdown',
                style={'width': '50%', 'marginBottom': 20}
            )
        ])
    ], style={'marginBottom': 30}),
    
    # Visualization section
    html.Div([
        # Left column - Scatter plot
        html.Div([
            dcc.Graph(id='scatter-plot')
        ], style={'width': '60%', 'display': 'inline-block'}),
        
        # Right column - Country details and stats
        html.Div([
            dcc.Graph(id='country-details'),
            html.Div(id='country-stats', style={'padding': '20px', 'backgroundColor': '#f8f9fa'})
        ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top'})
    ], style={'display': 'flex'})
], style={'padding': '20px', 'fontFamily': 'Arial'})

# Callback to update country dropdown based on year
@app.callback(
    [Output('country-dropdown', 'options'),
     Output('country-dropdown', 'value')],
    [Input('year-slider', 'value')]
)
def update_country_dropdown(selected_year):
    available_countries = df[df['year'] == selected_year]['Country'].unique()
    options = [{'label': country, 'value': country} for country in available_countries]
    return options, available_countries[0]

# Callback to update graphs
@app.callback(
    [Output('scatter-plot', 'figure'),
     Output('country-details', 'figure'),
     Output('country-stats', 'children')],
    [Input('year-slider', 'value'),
     Input('country-dropdown', 'value')]
)
def update_graphs(selected_year, selected_country):
    # Filter data for selected year
    year_data = df[df['year'] == selected_year]
    
    # Create scatter plot
    scatter_fig = px.scatter(
        year_data,
        x='GDP',
        y='total_medals',
        title=f'GDP vs Total Medals Distribution ({selected_year})',
        hover_data=['Country'],
        log_x=True,
        size='total_medals',
        color='total_medals',
        labels={'GDP': 'GDP (USD)', 'total_medals': 'Total Medals'},
        template='plotly_white'
    )
    
    # Add trendline
    scatter_fig.add_traces(px.scatter(year_data, x='GDP', y='total_medals', trendline="ols").data)
    
    # Highlight selected country
    country_data = year_data[year_data['Country'] == selected_country]
    scatter_fig.add_trace(
        go.Scatter(
            x=[country_data['GDP'].iloc[0]],
            y=[country_data['total_medals'].iloc[0]],
            mode='markers+text',
            marker=dict(size=20, color='#e74c3c', symbol='star'),
            text=[selected_country],
            textposition="top center",
            name=selected_country,
            hovertemplate=(
                "<b>%{text}</b><br>" +
                "GDP: $%{x:,.0f}<br>" +
                "Medals: %{y}<br>" +
                "<extra></extra>"
            )
        )
    )
    
    # Update scatter plot layout
    scatter_fig.update_layout(
        title_x=0.5,
        plot_bgcolor='rgba(240,240,240,0.2)',
        paper_bgcolor='white',
        hoverlabel=dict(bgcolor="white"),
        hovermode='closest'
    )
    
    # Create bar chart
    bar_fig = go.Figure()
    bar_fig.add_trace(go.Bar(
        x=['GDP (Billions)', 'Total Medals'],
        y=[country_data['GDP'].iloc[0]/1e9, country_data['total_medals'].iloc[0]],
        marker_color=['#3498db', '#e74c3c'],
        text=[f'${country_data["GDP"].iloc[0]/1e9:,.1f}B', 
              f'{country_data["total_medals"].iloc[0]:.0f}'],
        textposition='auto',
    ))
    
    bar_fig.update_layout(
        title=f'{selected_country} Statistics ({selected_year})',
        plot_bgcolor='rgba(240,240,240,0.2)',
        paper_bgcolor='white',
        showlegend=False,
        height=400
    )
    
    # Calculate rankings
    total_countries = len(year_data)
    gdp_rank = year_data.sort_values('GDP', ascending=False)['Country'].tolist().index(selected_country) + 1
    medals_rank = year_data.sort_values('total_medals', ascending=False)['Country'].tolist().index(selected_country) + 1# filepath: c:\Users\ice\Documents\courseworks\dataviz\comp4010_project1\demographic.py
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Initialize the Dash app
app = dash.Dash(__name__)

# Load and process data
def load_data():
    results_df = pd.read_csv('datasets/country_results_df.csv')
    gdp_df = pd.read_csv('support_datasets/GDP.csv')
    
    # Melt GDP data to convert years from columns to rows
    gdp_melted = gdp_df.melt(
        id_vars=['Country', 'Country Code'],
        value_vars=[str(year) for year in range(1960, 2023)],
        var_name='year',
        value_name='GDP'
    )
    gdp_melted['year'] = pd.to_numeric(gdp_melted['year'])
    
    # Prepare results data
    results_df['year'] = pd.to_numeric(results_df['year'])
    medal_cols = ['awards_gold', 'awards_silver', 'awards_bronze']
    for col in medal_cols:
        results_df[col] = pd.to_numeric(results_df[col], errors='coerce').fillna(0)
    results_df['total_medals'] = results_df[medal_cols].sum(axis=1)
    
    # Merge datasets
    merged_df = pd.merge(
        results_df[['country', 'year', 'total_medals']], 
        gdp_melted[['Country', 'year', 'GDP']],
        left_on=['country', 'year'],
        right_on=['Country', 'year'],
        how='inner'
    )
    
    merged_df['GDP'] = pd.to_numeric(merged_df['GDP'], errors='coerce')
    merged_df.dropna(subset=['GDP'], inplace=True)
    
    return merged_df

# Load the data
df = load_data()

# Custom CSS styling
app.layout = html.Div([
    # Header section
    html.Div([
        html.H1("GDP vs Olympic Medals Analysis (1960-2022)", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 30}),
        html.P("Explore the relationship between country GDP and Olympic performance over time", 
               style={'textAlign': 'center', 'color': '#7f8c8d'})
    ], style={'marginBottom': 40}),
    
    # Controls section
    html.Div([
        # Year selector
        html.Div([
            html.Label("Select Year:", style={'fontWeight': 'bold', 'color': '#2c3e50'}),
            dcc.Slider(
                id='year-slider',
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].max(),
                marks={str(year): str(year) for year in df['year'].unique()},
                step=None
            )
        ], style={'width': '100%', 'marginBottom': 30}),
        
        # Country selector
        html.Div([
            html.Label("Select Country:", style={'fontWeight': 'bold', 'color': '#2c3e50'}),
            dcc.Dropdown(
                id='country-dropdown',
                style={'width': '50%', 'marginBottom': 20}
            )
        ])
    ], style={'marginBottom': 30}),
    
    # Visualization section
    html.Div([
        # Left column - Scatter plot
        html.Div([
            dcc.Graph(id='scatter-plot')
        ], style={'width': '60%', 'display': 'inline-block'}),
        
        # Right column - Country details and stats
        html.Div([
            dcc.Graph(id='country-details'),
            html.Div(id='country-stats', style={'padding': '20px', 'backgroundColor': '#f8f9fa'})
        ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top'})
    ], style={'display': 'flex'})
], style={'padding': '20px', 'fontFamily': 'Arial'})

# Callback to update country dropdown based on year
@app.callback(
    [Output('country-dropdown', 'options'),
     Output('country-dropdown', 'value')],
    [Input('year-slider', 'value')]
)
def update_country_dropdown(selected_year):
    available_countries = df[df['year'] == selected_year]['Country'].unique()
    options = [{'label': country, 'value': country} for country in available_countries]
    return options, available_countries[0]

# Callback to update graphs
@app.callback(
    [Output('scatter-plot', 'figure'),
     Output('country-details', 'figure'),
     Output('country-stats', 'children')],
    [Input('year-slider', 'value'),
     Input('country-dropdown', 'value')]
)
def update_graphs(selected_year, selected_country):
    # Filter data for selected year
    year_data = df[df['year'] == selected_year]
    
    # Create scatter plot
    scatter_fig = px.scatter(
        year_data,
        x='GDP',
        y='total_medals',
        title=f'GDP vs Total Medals Distribution ({selected_year})',
        hover_data=['Country'],
        log_x=True,
        size='total_medals',
        color='total_medals',
        labels={'GDP': 'GDP (USD)', 'total_medals': 'Total Medals'},
        template='plotly_white'
    )
    
    # Add trendline
    scatter_fig.add_traces(px.scatter(year_data, x='GDP', y='total_medals', trendline="ols").data)
    
    # Highlight selected country
    country_data = year_data[year_data['Country'] == selected_country]
    scatter_fig.add_trace(
        go.Scatter(
            x=[country_data['GDP'].iloc[0]],
            y=[country_data['total_medals'].iloc[0]],
            mode='markers+text',
            marker=dict(size=20, color='#e74c3c', symbol='star'),
            text=[selected_country],
            textposition="top center",
            name=selected_country,
            hovertemplate=(
                "<b>%{text}</b><br>" +
                "GDP: $%{x:,.0f}<br>" +
                "Medals: %{y}<br>" +
                "<extra></extra>"
            )
        )
    )
    
    # Update scatter plot layout
    scatter_fig.update_layout(
        title_x=0.5,
        plot_bgcolor='rgba(240,240,240,0.2)',
        paper_bgcolor='white',
        hoverlabel=dict(bgcolor="white"),
        hovermode='closest'
    )
    
    # Create bar chart
    bar_fig = go.Figure()
    bar_fig.add_trace(go.Bar(
        x=['GDP (Billions)', 'Total Medals'],
        y=[country_data['GDP'].iloc[0]/1e9, country_data['total_medals'].iloc[0]],
        marker_color=['#3498db', '#e74c3c'],
        text=[f'${country_data["GDP"].iloc[0]/1e9:,.1f}B', 
              f'{country_data["total_medals"].iloc[0]:.0f}'],
        textposition='auto',
    ))
    
    bar_fig.update_layout(
        title=f'{selected_country} Statistics ({selected_year})',
        plot_bgcolor='rgba(240,240,240,0.2)',
        paper_bgcolor='white',
        showlegend=False,
        height=400
    )
    # Add time series chart to country details
    years_data = df[df['Country'] == selected_country].sort_values('year')
    
    # Create time series subplot for country details
    time_series = make_subplots(
        rows=2, cols=1,
        subplot_titles=('GDP Over Time', 'Medals Over Time')
    )
    
    # Add GDP time series
    time_series.add_trace(
        go.Scatter(
            x=years_data['year'],
            y=years_data['GDP']/1e9,
            mode='lines+markers',
            name='GDP',
            line=dict(color='#3498db'),
            hovertemplate="Year: %{x}<br>GDP: $%{y:.1f}B<extra></extra>"
        ),
        row=1, col=1
    )
    
    # Add medals time series
    time_series.add_trace(
        go.Scatter(
            x=years_data['year'],
            y=years_data['total_medals'],
            mode='lines+markers',
            name='Medals',
            line=dict(color='#e74c3c'),
            hovertemplate="Year: %{x}<br>Medals: %{y}<extra></extra>"
        ),
        row=2, col=1
    )
    
    # Update time series layout
    time_series.update_layout(
        height=500,
        showlegend=False,
        plot_bgcolor='rgba(240,240,240,0.2)',
        paper_bgcolor='white',
        title=f'{selected_country} Historical Trends',
        title_x=0.5
    )
     # Calculate rankings (move this before stats_card creation)
    total_countries = len(year_data)
    gdp_rank = year_data.sort_values('GDP', ascending=False)['Country'].tolist().index(selected_country) + 1
    medals_rank = year_data.sort_values('total_medals', ascending=False)['Country'].tolist().index(selected_country) + 1
    # Create stats card with historical context
    stats_card = html.Div([
        html.H4('Country Performance', style={'marginBottom': '15px', 'color': '#2c3e50'}),
        html.Div([
            html.P([
                'Current GDP Rank: ',
                html.Strong(f'{gdp_rank}/{total_countries}')
            ]),
            html.P([
                'Current Medals Rank: ',
                html.Strong(f'{medals_rank}/{total_countries}')
            ]),
            html.P([
                'Historical Best Year: ',
                html.Strong(f"{years_data.loc[years_data['total_medals'].idxmax(), 'year']}")
            ]),
            html.P([
                'Total Historical Medals: ',
                html.Strong(f"{years_data['total_medals'].sum():.0f}")
            ])
        ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '5px'})
    ])
    
    return scatter_fig, time_series, stats_card

if __name__ == '__main__':
    app.run(debug=True)