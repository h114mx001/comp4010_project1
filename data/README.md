# International Mathematical Olympiad (IMO) Dataset

This dataset captures the complete historical records of the International Mathematical Olympiad (IMO) from its inception in 1959 through 2024. The IMO is the premier international mathematics competition for high school students, held annually with participation from over 100 countries.

The dataset is curated as part of the TidyTuesday project (Week 39, 2024) and was originally compiled by Havisha Khurana. Special thanks to Emi Tanaka for helping improve data accuracy.

## Dataset Overview

The dataset is split into three components:

### 1. `country_results_df.csv`
Contains team-level information per participating country per year, including:
- Participation statistics (`team_size_all`, `team_size_male`, `team_size_female`)
- Scores on problems (`p1` to `p7`)
- Medal counts (`awards_gold`, `awards_silver`, `awards_bronze`, `awards_honorable_mentions`)
- Team leadership (`leader`, `deputy_leader`)

### 2. `individual_results_df.csv`
Contains detailed results for individual contestants, including:
- Problem-level scores (`p1` to `p6`)
- Total score (`total`), rank (`individual_rank`), and awarded medal (`award`)
- Country and contestant name

### 3. `timeline_df.csv`
Captures metadata for each edition of the IMO, such as:
- Year, host country and city
- Number of countries and contestants
- Gender breakdown (`male_contestant`, `female_contestant`)
- Start and end dates

## Example Questions This Dataset Can Help Answer

- How have country rankings shifted over time?
- What are the historical trends in gender participation?
- How do team size or composition relate to overall team performance?
- Is there a relationship between socioeconomic indicators and IMO success?

## Data Access

You can load the data using the `tidytuesdayR` package:

```r
## Option 1: tidytuesdayR
install.packages("tidytuesdayR")
tuesdata <- tidytuesdayR::tt_load('2024-09-24')
country_results_df <- tuesdata$country_results_df
individual_results_df <- tuesdata$individual_results_df
timeline_df <- tuesdata$timeline_df

## Option 2: Read directly from GitHub
country_results_df <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2024/2024-09-24/country_results_df.csv')
individual_results_df <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2024/2024-09-24/individual_results_df.csv')
timeline_df <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2024/2024-09-24/timeline_df.csv')
