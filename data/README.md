# International Mathematical Olympiad (IMO) Dataset

## Overview

This dataset provides comprehensive historical data from the **International Mathematical Olympiad (IMO)**, the world championship mathematics competition for high school students. Held annually since **1959**, the IMO brings together top-performing students from over 100 countries to solve six challenging math problems over two consecutive days.

The data spans from **1959 to 2024** and is sourced from public IMO archives, curated as part of the [#TidyTuesday](https://github.com/rfordatascience/tidytuesday) project (Week 39, 2024), with contributions from **Havisha Khurana** and quality improvements from **Emi Tanaka**.

The dataset is structured into three files:

1. `country_results_df.csv` – country-level performance and team composition.
2. `individual_results_df.csv` – individual performance data.
3. `timeline_df.csv` – metadata and participation summaries per year.

---

## Dataset Access

You can load the dataset using the **`tidytuesdayR`** R package:

```r
# Option 1: Using tidytuesdayR
install.packages("tidytuesdayR")
tuesdata <- tidytuesdayR::tt_load('2024-09-24')

country_results_df <- tuesdata$country_results_df
individual_results_df <- tuesdata$individual_results_df
timeline_df <- tuesdata$timeline_df

# Option 2: Direct GitHub download
readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2024/2024-09-24/country_results_df.csv')
readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2024/2024-09-24/individual_results_df.csv')
readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2024/2024-09-24/timeline_df.csv')
```

---

## Codebook

### `country_results_df.csv`

| Variable                   | Type     | Description                                                   |
|----------------------------|----------|---------------------------------------------------------------|
| `year`                    | Integer  | Year of the IMO edition                                       |
| `country`                 | String   | Name of participating country                                 |
| `team_size_all`           | Integer  | Total number of participants from the country                 |
| `team_size_male`          | Integer  | Number of male participants                                   |
| `team_size_female`        | Integer  | Number of female participants                                 |
| `p1` to `p6`, `p7`        | Integer  | Team's aggregated score on each problem (1–7 where applicable)|
| `awards_gold`             | Integer  | Number of gold medals won                                     |
| `awards_silver`           | Integer  | Number of silver medals won                                   |
| `awards_bronze`           | Integer  | Number of bronze medals won                                   |
| `awards_honorable_mentions` | Integer| Number of honorable mentions received                         |
| `leader`                  | String   | Name of team leader                                           |
| `deputy_leader`           | String   | Name of deputy team leader                                    |

---

### `individual_results_df.csv`

| Variable          | Type     | Description                                           |
|-------------------|----------|-------------------------------------------------------|
| `year`           | Integer  | Year of the IMO edition                               |
| `contestant`     | String   | Name of the individual contestant                     |
| `country`        | String   | Country represented by the contestant                 |
| `p1` to `p6`     | Integer  | Scores obtained on problems 1 through 6               |
| `total`          | Integer  | Total score across all problems                       |
| `individual_rank`| Integer  | Global rank of the contestant                         |
| `award`          | String   | Award received (e.g., Gold, Silver, Bronze, HM, None) |

---

### `timeline_df.csv`

| Variable            | Type     | Description                                               |
|---------------------|----------|-----------------------------------------------------------|
| `edition`          | Integer  | Edition number (e.g., 1st IMO = 1959)                     |
| `year`             | Integer  | Year of the competition                                   |
| `country`          | String   | Host country                                              |
| `city`             | String   | Host city                                                 |
| `countries`        | Integer  | Number of countries that participated                     |
| `all_contestant`   | Integer  | Total number of contestants                               |
| `male_contestant`  | Integer  | Total number of male contestants                          |
| `female_contestant`| Integer  | Total number of female contestants                        |
| `start_date`       | Date     | Start date of the IMO                                     |
| `end_date`         | Date     | End date of the IMO                                       |

---

## Limitations

- **Missing data**: Some early years lack complete gender or score breakdowns.
- **Scoring formats**: A few years have an additional 7th problem (`p7`), which is rare.
- **Demographics**: Individual-level demographic variables such as age and gender are not provided.

Despite these issues, the dataset offers rich opportunities for studying trends in global STEM education, performance patterns, gender participation, and the influence of national policies and contexts on academic competitions.

---

## Attribution

Curated by **Havisha Khurana** for [TidyTuesday](https://github.com/rfordatascience/tidytuesday) (Week 39, 2024). Bug fixes by **Emi Tanaka**.

---


