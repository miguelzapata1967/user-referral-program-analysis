# User Referral Program --- Business & Data Analysis

## Objective

This project evaluates customer and transaction behavior surrounding the
referral-program launch on **October 31, 2015**, including before/after
activity, new-user referral behavior, spending, transaction frequency,
existing-user behavior, and daily trends.

## Data Quality Findings

The original dataset contained **97,341 records**. The audit identified
**24 exact duplicate copies**, leaving **97,317 analytical records**.

Validation identified **0 invalid dates, 0 missing values, 0 blank
country values, 0 blank device IDs, 0 invalid referral indicators, 0
referral transactions before launch, 0 negative spending amounts, and 0
zero-dollar transactions**.

The valid observation period is **October 3 through November 27, 2015**.

The data contains **18,809 unique users** and **17,887 unique devices**.
There were **3,883 users associated with multiple devices** and **3,988
devices associated with multiple users**, with a maximum of **6 users
associated with one device**. These were retained as audit findings
without assigning an unsupported explanation.

## Before vs. After Launch

  Metric                       Before         After
  --------------------- ------------- -------------
  Transactions                 47,320        49,997
  Unique Users                  5,000        18,397
  Total Spending          \$2,005,687   \$2,343,881
  Average Transaction         \$42.39       \$46.88

Average transaction value increased approximately **\$4.49**, or
**10.6%**.

These are observed before/after differences. Because the data is
observational rather than randomized, the analysis does not attribute
the entire change to the referral program.

## Existing vs. New Users

Of **18,397 users active after launch**, **4,588** were existing users
who also appeared before launch and **13,809** appeared for the first
time after launch.

Approximately **75.1%** of post-launch users were newly observed.

## New-User Referral Behavior

  New-User Group                          Users      Share
  -------------------------------- ------------ ----------
  Referral Only                           6,858      49.7%
  Non-Referral Only                       1,094       7.9%
  Both Referral and Non-Referral          5,857      42.4%
  **Total**                          **13,809**   **100%**

A total of **12,715 new users (approximately 92.1%)** had at least one
referral transaction.

This demonstrates high referral participation among newly observed
users. It does not by itself prove that referrals caused those users to
join.

## New-User Business Value

  ------------------------------------------------------------------------------------------------------
  Group               Users   Transactions       Total          Avg.            Avg.                Avg.
                                              Spending   Transaction   Spending/User   Transactions/User
  -------------- ---------- -------------- ----------- ------------- --------------- -------------------
  Referral Only       6,858         15,120   \$710,397       \$46.98        \$103.59                2.20

  Non-Referral        1,094          1,483    \$68,606       \$46.26         \$62.71                1.36
  Only                                                                               

  Both                5,857         20,788   \$974,964       \$46.90        \$166.46                3.55
  ------------------------------------------------------------------------------------------------------

Average transaction value was similar across all three groups, at
approximately **\$46--\$47**.

The larger difference was transaction frequency. Users participating in
both referral and non-referral activity averaged **3.55 transactions per
user**, compared with **2.20** for referral-only users and **1.36** for
non-referral-only users.

The Both group therefore produced the highest average spending per user
at **\$166.46**, driven primarily by greater transaction frequency
rather than substantially larger individual transactions.

## Existing Users Before vs. After

  Metric                             Before       After
  --------------------------- ------------- -----------
  Users                               4,588       4,588
  Transactions                       43,354      12,606
  Total Spending                \$1,837,674   \$589,914
  Average Transaction               \$42.39     \$46.80
  Average Transactions/User            9.45        2.75

Existing users had a higher average transaction value after launch,
while their observed transaction frequency was substantially lower.

The daily existing-user analysis also showed a clear reduction in
existing-user transaction volume during the post-launch observation
period. Therefore, the overall post-launch results should not be
interpreted as every customer becoming more active.

## Daily Trend Analysis

Daily transactions and spending displayed strong repeating weekly
patterns. Similar peaks were already present before the referral-program
launch, so those recurring peaks should not automatically be attributed
to the program.

Daily average transaction value showed a visible level change around
launch. The aggregate average increased from **\$42.39 before launch to
\$46.88 after launch**.

## Business Interpretation

The referral-program period coincided with a substantial expansion in
the observed user population and high referral participation among newly
observed users.

Referral-involved new users also demonstrated greater transaction
frequency and spending per user than the non-referral-only group. Users
participating in both referral and non-referral transactions showed the
highest observed engagement.

At the same time, existing users became less transaction-active during
the post-launch observation period despite having a higher average
transaction value.

Program performance should therefore be monitored with multiple
measures, including **new-user acquisition, referral participation,
transactions per user, spending per user, average transaction value, and
existing-user activity/retention**.

## Limitations

This analysis is **observational**, not a randomized experiment. There
is no randomized control group, so post-launch changes cannot be
attributed exclusively to the referral program.

The dataset also does not explain why some users share devices, why some
users use multiple devices, or what external marketing, seasonal,
business, or operational factors may have changed during the observation
period.

The analysis therefore distinguishes observed evidence from causal
conclusions.

## Technical Documentation

The complete Python workflow, validation procedures, calculations, and
visualization process are documented in
**[readme_tech.md](readme_tech.md)**.
