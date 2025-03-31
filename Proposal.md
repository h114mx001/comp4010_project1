# COMP4010 Project 1 - Proposal 

## The dataset 

The dataset is curated from [International Mathematics Olympiad](https://www.imo-official.org/) (IMO). The competition is held annually by countries around the world. Since its first time in 1959 in Romania, the competition has been a prestigious event for high school students to showcase their mathematical skills. The competition consists of 06 problems, over 02 consecutive days with 03 problems each. 

The dataset is the record of the competition from 1959 to 2024, for both countries and individual results. 

The [country results datasets](./datasets/country_results_df.csv) contain the following columns: 

|variable                  |class     |description                           |
|:-------------------------|:---------|:-------------------------------------|
|year                      |integer   |Year of IMO |
|country                   |character |Participating country |
|team_size_all             |integer   |Participating contestants |
|team_size_male            |integer   |Male contestants |
|team_size_female          |integer   |Female contestants|
|p1                        |integer   |Score on problem 1 |
|p2                        |integer   |Score on problem 2 |
|p3                        |integer   |Score on problem 3 |
|p4                        |integer   |Score on problem 4 |
|p5                        |integer   |Score on problem 5 |
|p6                        |integer   |Score on problem 6 |
|p7                        |integer   |Score on problem 7 |
|awards_gold               |integer   |Number of gold medals |
|awards_silver             |integer   |Number of silver medals |
|awards_bronze             |integer   |Number of bronze medals |
|awards_honorable_mentions |integer   |Number of honorable mentions |
|leader                    |character |Leader of country team |
|deputy_leader             |character |Deputy leader of country team |


The [individual results datasets](./datasets/individual_results_df.csv) contain the following columns:

|variable        |class     |description                           |
|:---------------|:---------|:-------------------------------------|
|year            |integer   |Year of IMO  |
|contestant      |character |Participant's name |
|country         |character |Participant's country |
|p1              |integer   |Score on problem 1 |
|p2              |integer   |Score on problem 2 |
|p3              |integer   |Score on problem 3 |
|p4              |integer   |Score on problem 4 |
|p5              |integer   |Score on problem 5 |
|p6              |integer   |Score on problem 6 |
|total           |integer   |Total score on all problems |
|individual_rank |integer   |Individual rank |
|award           |character |Award won |

The [timeline datasets](./datasets/timeline_df.csv) contain the following columns:

|variable          |class     |description                           |
|:-----------------|:---------|:-------------------------------------|
|edition           |integer   |Edition of International Mathematical Olympiad (IMO) |
|year              |integer   |Year of IMO |
|country           |character |Host country |
|city              |character |Host city |
|countries         |integer   |Number of participating countries|
|all_contestant    |integer   |Number of participating contestants|
|male_contestant   |integer   |Number of participating male contestants |
|female_contestant |integer   |Number of participating female contestants |
|start_date        |Date      |Start date of IMO |
|end_date          |Date      |End date of IMO |

## Why this dataset?


Scientific high school competitions like IMO serve as critical motivational platforms for students to engage with mathematics and other foundational STEM subjects. Analyzing the IMO's historical data provides a unique window into several important dimensions:

1. **Educational Systems Evaluation**: Performance patterns across countries can reveal strengths and weaknesses in various educational approaches to mathematics instruction.
2. **Cultural and Socioeconomic Influences**: Participation and achievement trends may reflect cultural attitudes toward mathematics education and correlate with socioeconomic factors.
3. **Gender Equality in STEM**: The dataset's gender metrics offer opportunities to examine the historical progression of female participation in elite mathematics competitions.
4. **Geopolitical Context**: The 65-year span captures significant world events (Cold War, formation of new nations, globalization) that influenced international academic competition.
5. **Educational Policy Implications**: Insights from this analysis could inform policy recommendations for improving mathematics education and increasing diverse participation in STEM fields.

This analysis holds particular relevance in today's knowledge economy, where mathematical literacy and problem-solving skills are increasingly valued across sectors and industries

## Research Questions

Our project is structured around two complementary research questions that allow for both historical trend analysis and demographic investigation:

### Research Question 1: Competition Evolution

How has the International Mathematics Olympiad evolved over its 65-year history in terms of:

- Global participation patterns (number of countries, regional representation)
- Contestant demographics (total participants, gender distribution)
- Competition structure (hosting patterns, problem difficulty trends)
- Performance metrics (score distributions, medal allocations)

We aim to identify key inflection points in the competition's development and correlate these with historical contexts and events. This longitudinal analysis will reveal how this premier mathematical competition has grown from a regional event to a truly global phenomenon.

### Research Question 2: Participation Demographics Analysis

What significant patterns emerge when analyzing IMO participation and performance through demographic lenses:

- **Gender Distribution**: How has female participation evolved over time and across regions?
- **Geographic Representation**: Which regions show consistent participation versus emerging presence?
- **Socioeconomic Factors**: How do external factors (GDP, education spending, development indices) correlate with participation and performance?
- **Performance Equity**: Is there evidence of performance gaps based on demographic factors?

Through this analysis, we hope to uncover insights about barriers to participation and factors contributing to mathematical achievement at the international level.

## Methodology

### Data Preparation and Preprocessing

Our methodology will follow a structured approach:

1. **Data Cleaning**:
    - Standardize country names to account for geopolitical changes
    - Handle missing values through appropriate imputation techniques
    - Validate data consistency across years
    - Remove outliers or erroneous entries
2. **Feature Engineering**:
    - Create derived metrics (performance indices, gender ratios)
    - Normalize scores across competition years if scoring systems changed
    - Generate temporal and geographical aggregations
    - Develop composite indicators for comparative analysis
3. **Integration with External Data**:
    - Source and integrate relevant socioeconomic indicators from World Bank or UN datasets
    - Include educational spending metrics where available
    - Incorporate historical context markers for significant world events

### Analytical Approaches

For Question 1 (Competition Evolution):

- Time series analysis of participation metrics
- Trend identification and change point detection
- Visualization of geographical expansion through interactive mapping
- Statistical analysis of score distributions over time

For Question 2 (Demographics Analysis):

- Correlation analysis between socioeconomic factors and participation/performance
- Gender participation trend analysis with regional breakdowns
- Multivariate analysis to identify factors influencing performance
- Comparative analysis of high-performing countries relative to resources


## Tentative plan

### Phase 1: Data Acquisition and Preparation

- Collect and consolidate IMO datasets from all available years
- Clean and standardize data formats
- Source supplementary socioeconomic datasets
- Develop data dictionary and validation protocols


### Phase 2: Exploratory Analysis

- Generate descriptive statistics for all variables
- Create preliminary visualizations for key metrics
- Identify trends and patterns for further investigation
- Develop working hypotheses based on initial findings


### Phase 3: In-Depth Analysis

- Conduct detailed statistical analysis for both research questions
- Develop comprehensive visualization suite
- Test hypotheses and document findings
- Integrate socioeconomic factors into the analysis


### Phase 4: Synthesis and Presentation

- Compile findings into cohesive narrative
- Create final visualizations and interactive components
- Prepare documentation and presentations
- Extract actionable insights and recommendations

## Expected Outcomes

This project will deliver:

1. A comprehensive analysis of IMO trends over 65 years, revealing patterns in mathematical competition at the international level
2. Insights into demographic factors affecting participation and performance in elite mathematics
3. Interactive data visualizations allowing exploration of historical trends and patterns
4. Potential policy recommendations for increasing diverse participation in mathematics
5. A reproducible methodology for analyzing international academic competitions

## Conclusion

The International Mathematics Olympiad dataset offers a rich opportunity to examine the evolution of mathematical competition on the global stage while investigating factors that influence participation and success. By combining historical trend analysis with demographic investigation, our project aims to contribute meaningful insights to the understanding of mathematical education and talent development across diverse global contexts.

Through careful methodology and comprehensive analysis, we expect to uncover patterns that may inform educational policy and practice, particularly regarding strategies to foster mathematical talent across different demographic groups and regions. This work holds relevance not only for mathematics education specifically but for broader questions of equity and excellence in STEM fields globally.
