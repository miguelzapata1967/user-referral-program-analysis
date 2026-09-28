# User Referral Program --- Technical Analysis & Data Quality

## Technology

The project was completed with **Python, Pandas, Matplotlib, and Visual
Studio Code**.

Main analysis script: `Scripts/user_referral_program_project.py`

Source data: `Data/referral.csv`

Generated charts: `Graphics/`

## Dataset Fields

  Field           Purpose
  --------------- -----------------------------
  `user_id`       User identifier
  `date`          Transaction date
  `country`       Country field
  `money_spent`   Transaction monetary amount
  `is_referral`   Referral indicator: 0 or 1
  `device_id`     Device identifier

## Duplicate Audit

The raw dataset contained **97,341 rows**. Exact duplicate detection
identified **24 duplicate copies**.

After `drop_duplicates()`, the analytical dataset contained **97,317
rows**.

Repeated transactions by the same user were preserved. Only exact
duplicate records were removed.

## Date Validation

Dates were tested with:

``` python
pd.to_datetime(df_clean["date"], errors="coerce")
```

Results: - Invalid dates: **0** - Earliest date: **2015-10-03** - Latest
date: **2015-11-27**

## Referral Validation

The `is_referral` field was checked to confirm values were limited to 0
and 1.

-   Non-referral records: **69,302**
-   Referral records: **28,015**
-   Invalid referral values: **0**
-   Referral transactions before launch: **0**
-   Referral transactions on/after launch: **28,015**

Launch date:

``` python
launch_date = pd.Timestamp("2015-10-31")
```

October 31 is treated as part of the post-launch period.

## Launch-Day Audit

October 31 contained **3,233 transactions** from **2,963 unique users**.

Referral status: - Non-referral transactions: **1,423** - Referral
transactions: **1,810**

## Missing and Blank Values

All six columns were checked for null values. The `country` and
`device_id` text fields were also checked for blank strings. No missing
or blank values were identified.

## Money-Spent Validation

-   Minimum: **\$10**
-   Maximum: **\$220**
-   Mean: **\$44.69**
-   Median: **\$42**
-   Negative amounts: **0**
-   Zero amounts: **0**

Large transactions were reviewed rather than automatically deleted
because the dataset did not establish that they were invalid.

## User and Device Audit

-   Unique users: **18,809**
-   Unique devices: **17,887**
-   Users associated with multiple devices: **3,883**
-   Devices associated with multiple users: **3,988**
-   Maximum users associated with one device: **6**

These relationships were documented without assuming fraud, household
sharing, device recycling, or another unsupported explanation.

## Analytical Methodology

### Before/After Segmentation

The clean data was divided into: - **Before launch:** dates earlier than
October 31, 2015 - **After launch:** October 31, 2015 and later

For each period, the script calculated transaction count, unique users,
total spending, and average transaction value.

### Existing and New Users

Post-launch users were classified as: - **Existing users:** appeared
before launch and remained active after launch - **New users:** first
appeared after launch

Results: - Existing users active after launch: **4,588** - Newly
observed users: **13,809**

### New-User Referral Segmentation

New users were separated into mutually exclusive groups: - Referral
Only - Non-Referral Only - Both Referral and Non-Referral

For each group, the analysis calculated users, transactions, total
spending, average transaction value, average spending per user, and
average transactions per user.

### Existing-User Comparison

The same **4,588 existing users** were isolated for the before/after
comparison.

The analysis calculated transactions, total spending, average
transaction value, and average transactions per user.

A daily existing-user table also calculated: - Daily transactions -
Daily active users - Daily total spending - Transactions per active user

## Python Visualizations

The project generated **10 graphics** in the `Graphics` directory:

1.  `graph_01_before_after_transactions.png`
2.  `graph_02_existing_vs_new_users.png`
3.  `graph_03_new_user_referral_behavior.png`
4.  `graph_04_total_spending_by_group.png`
5.  `graph_05_average_spending_per_user.png`
6.  `graph_06_average_transactions_per_user.png`
7.  `graph_07_daily_transactions.png`
8.  `graph_08_daily_spending.png`
9.  `graph_09_daily_average_transaction.png`
10. `graph_10_existing_user_daily_transactions.png`

The time-series graphics mark the referral-program launch date to make
the before/after boundary visible.

## Analytical Safeguards

The project deliberately: - Removed exact duplicates while preserving
legitimate repeated activity. - Preserved high-value transactions when
no evidence showed they were invalid. - Documented shared devices
without assigning an unsupported cause. - Separated existing and newly
observed users. - Distinguished referral participation from proof of
referral-caused acquisition. - Avoided attributing recurring weekly
peaks to the referral program when those patterns existed before
launch. - Treated before/after results as observational rather than
randomized experimental evidence.

## Reproducible Workflow

**CSV → Pandas validation and cleaning → user segmentation → metric
calculation → daily trend analysis → Matplotlib graphics → documented
findings**

For the business findings and interpretation, see
**[readme_analysis.md](readme_analysis.md)**.
