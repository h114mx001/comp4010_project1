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

Scientific high school competitions like IMO are great motivations for students to learn and practice mathematics, as well as other foundational subjects. On the other hand, understanding the competition's history and the performance records of participating countries may provide insights into some aspects such as education system, culture, and even social-economic status. Moreover, as the datasets providing some metrics such as male vs. female contestants, scores, etc., we can analyze some deeper insights on gender equality. Finally, understanding the insights from the dataset may help us to know more on, at least locally, how to improve the education system to foster the students' potential in mathematics.

## Two questions 

1. Given the starting year of the competition, as well as the changing history of the world, how has the competition evolved (in terms of participating countries, number of contestants, etc.) over the years? 

2. What is the distribution of participation based on:
   1. Genders?
   2. Countries?
   3. Social-economic status?
   4. Other factors?

## Tentative plan

1. For question 1: 
    - Data cleaning and preprocessing
    - Exploratory data analysis
    - Adding columns (average score, etc.) for better analysis
    - Drop columns that are not useful for the analysis (e.g., leader, deputy leader)

2. For question 2: 
    - Data cleaning and preprocessing
    - Exploratory data analysis
    - Adding columns from other datasets (e.g. GDP per capita, etc.) for understanding the social-economic status
    - Drop columns that are not useful for the analysis (e.g., leader, deputy leader)

For both questions:
    - Visualization
    - Hypothesis testing
    - Conclusion
