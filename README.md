## Project Context & AI Assistance

This project was completed as part of my Data Engineering Academy studies and used as a learning exercise in operational analytics, demand forecasting, and inventory planning.

I used AI tools, including Claude, to help work through the project and understand the analytical methods. **Claude performed the analysis, including the advanced forecasting, calculations, and generation of recommendations.** These outputs are shared as AI-assisted educational work; I do not claim to have independently built or validated all of the models.

My participation involved working with Python with AI assistance, asking questions, studying the outputs, and learning how analytical results relate to operational decisions. Including this project in my portfolio documents that learning process and my developing ability to question assumptions, interpret results, and explain business implications.

ChatGPT/Codex assisted with organizing and writing the project documentation. The reported results remain subject to the limitations and validation needs described in the analysis and technical documents.



# User Referral Program Analysis

## Project Overview

This project analyzes transaction activity surrounding the launch of a
user referral program on **October 31, 2015**. The analysis focuses on
data quality, customer activity before and after launch, new-user
referral behavior, spending, transaction frequency, and existing-user
behavior.

The dataset covers **October 3 through November 27, 2015**.

## Project Structure

-   `README.md` --- Project overview and navigation
-   `readme_analysis.md` --- Business analysis, findings,
    interpretation, and limitations
-   `readme_tech.md` --- Technical workflow, validation methodology,
    Python calculations, and graphics
-   `Scripts/user_referral_program_project.py` --- Python analysis
-   `Data/referral.csv` --- Source dataset
-   `Graphics/` --- Python-generated visualizations

## Key Results

The raw dataset contained **97,341 transactions**. After removing **24
exact duplicate copies**, the analytical dataset contained **97,317
records**.

Before launch, the dataset recorded **47,320 transactions**, **5,000
users**, and **\$2,005,687** in spending. After launch, it recorded
**49,997 transactions**, **18,397 users**, and **\$2,343,881** in
spending.

Among **13,809 newly observed users after launch**, **12,715
(approximately 92.1%)** had at least one referral transaction.

Users participating in both referral and non-referral activity showed
the highest observed new-user engagement, averaging **3.55
transactions** and **\$166.46 in spending per user**.

Because this is an observational before/after analysis rather than a
randomized experiment, the findings demonstrate associations during the
referral-program period but do not establish that the referral program
alone caused the observed changes.

## Documentation

For the complete business interpretation, see
**[readme_analysis.md](readme_analysis.md)**.

For the Python workflow, validation methodology, calculations, and
graphics, see **[readme_tech.md](readme_tech.md)**.
