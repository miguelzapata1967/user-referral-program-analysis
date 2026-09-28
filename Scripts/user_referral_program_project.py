# ===========================================================================================
#  checking dataframes structure and data types
# ===========================================================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Folder for saved graphics
output_folder = Path(__file__).resolve().parent.parent / "Graphics"
output_folder.mkdir(exist_ok=True)


# ===========================================================================================
#  Importing dataframes 
# ===========================================================================================

df = pd.read_csv(r'C:\Users\mexar\OneDrive\DE_Academy\User_Referral_Program\Data\referral.csv')

# ===========================================================================================
#  checking dataframes structure and data types
# ===========================================================================================

print (df.head())

print("\n--- DUPLICATE CHECK ---")

# Exact duplicate rows
exact_duplicates = df.duplicated().sum()
print("Exact duplicate rows:", exact_duplicates)

# Number of unique users
unique_users = df["user_id"].nunique()
print("Unique users:", unique_users)

# Total transactions
print("Total transactions:", len(df))

# Users with more than one transaction
transactions_per_user = df["user_id"].value_counts()

repeat_users = (transactions_per_user > 1).sum()
print("Users with multiple transactions:", repeat_users)

# Maximum transactions made by one user
print("Maximum transactions by one user:", transactions_per_user.max())

# Show all exact duplicate records
duplicate_rows = df[df.duplicated(keep=False)]

print("\n--- EXACT DUPLICATE RECORDS ---")
print(duplicate_rows.sort_values(["user_id", "date"]))

# -----------------------------------
# REMOVE EXACT DUPLICATE ROWS
# -----------------------------------

raw_rows = len(df)

df_clean = df.drop_duplicates().copy()

clean_rows = len(df_clean)
removed_duplicates = raw_rows - clean_rows

print("\n--- DUPLICATE CLEANING ---")
print("Raw rows:", raw_rows)
print("Exact duplicate copies removed:", removed_duplicates)
print("Rows after duplicate cleaning:", clean_rows)

# Verify duplicates are gone
print("Exact duplicates remaining:",
      df_clean.duplicated().sum())

# -----------------------------------
# DATA TYPE CHECK
# -----------------------------------

print("\n--- DATA TYPE CHECK ---")
print(df_clean.dtypes)

# -----------------------------------
# DATE VALIDATION
# -----------------------------------

print("\n--- DATE VALIDATION ---")

# Convert dates safely
date_test = pd.to_datetime(df_clean["date"], errors="coerce")

# Convert the actual date column after validation
df_clean["date"] = pd.to_datetime(df_clean["date"])

# -----------------------------------
# REFERRAL PROGRAM BUSINESS RULE CHECK
# -----------------------------------

print("\n--- REFERRAL PROGRAM VALIDATION ---")

# Define program launch date
launch_date = pd.Timestamp("2015-10-31")

# Verify referral field contains only 0 and 1
print("\nReferral values:")
print(df_clean["is_referral"].value_counts().sort_index())

invalid_referral = ~df_clean["is_referral"].isin([0, 1])

print("\nInvalid referral values:", invalid_referral.sum())

# Check referrals before launch
referrals_before_launch = df_clean[
    (df_clean["date"] < launch_date) &
    (df_clean["is_referral"] == 1)
]

print("Referral transactions before launch:",
      len(referrals_before_launch))

# Check referrals on or after launch
referrals_after_launch = df_clean[
    (df_clean["date"] >= launch_date) &
    (df_clean["is_referral"] == 1)
]

print("Referral transactions on/after launch:",
      len(referrals_after_launch))


# -----------------------------------
# LAUNCH DAY CHECK
# -----------------------------------

launch_day = df_clean[
    df_clean["date"] == launch_date
]

print("\n--- LAUNCH DAY CHECK ---")

print("Transactions on October 31:",
      len(launch_day))

print("Unique users on October 31:",
      launch_day["user_id"].nunique())

print("\nReferral status on October 31:")
print(
    launch_day["is_referral"]
    .value_counts()
    .sort_index()
)

# -----------------------------------
# MISSING AND BLANK VALUE CHECK
# -----------------------------------

print("\n--- MISSING VALUE CHECK ---")

print("\nNull values:")
print(df_clean.isnull().sum())

print("\nBlank text values:")

text_columns = ["country", "device_id"]

for column in text_columns:
    blank_count = (
        df_clean[column]
        .astype(str)
        .str.strip()
        .eq("")
        .sum()
    )

    print(column, ":", blank_count)

    # -----------------------------------
# MONEY SPENT VALIDATION
# -----------------------------------

print("\n--- MONEY SPENT VALIDATION ---")

print("Minimum amount:",
      df_clean["money_spent"].min())

print("Maximum amount:",
      df_clean["money_spent"].max())

print("Average amount:",
      df_clean["money_spent"].mean())

print("Median amount:",
      df_clean["money_spent"].median())

print("Negative amounts:",
      (df_clean["money_spent"] < 0).sum())

print("Zero amounts:",
      (df_clean["money_spent"] == 0).sum())

print("\nMoney spent statistics:")
print(df_clean["money_spent"].describe())

# Show the 10 largest transactions
print("\n--- TOP 10 LARGEST TRANSACTIONS ---")

largest_transactions = df_clean.nlargest(
    10,
    "money_spent"
)

print(
    largest_transactions[
        [
            "user_id",
            "date",
            "country",
            "money_spent",
            "is_referral",
            "device_id"
        ]
    ]
)

# -----------------------------------
# USER AND DEVICE VALIDATION
# -----------------------------------

print("\n--- USER AND DEVICE VALIDATION ---")

unique_users = df_clean["user_id"].nunique()
unique_devices = df_clean["device_id"].nunique()

print("Unique users:", unique_users)
print("Unique devices:", unique_devices)


# How many devices does each user use?
devices_per_user = (
    df_clean.groupby("user_id")["device_id"]
    .nunique()
)

users_multiple_devices = (
    devices_per_user > 1
).sum()

print(
    "Users associated with multiple devices:",
    users_multiple_devices
)


# How many users are associated with each device?
users_per_device = (
    df_clean.groupby("device_id")["user_id"]
    .nunique()
)

devices_multiple_users = (
    users_per_device > 1
).sum()

print(
    "Devices associated with multiple users:",
    devices_multiple_users
)

print(
    "Maximum users associated with one device:",
    users_per_device.max()
)

print("\n--- MOST SHARED DEVICES ---")

shared_devices = (
    users_per_device
    .sort_values(ascending=False)
    .head(10)
)

print(shared_devices)

date_test = pd.to_datetime(df_clean["date"], errors="coerce")
invalid_dates = date_test.isna().sum()

print("Invalid dates:", invalid_dates)

print("Earliest date:", date_test.min())
print("Latest date:", date_test.max())

df_clean["date"] = pd.to_datetime(df_clean["date"])

# -----------------------------------
# BEFORE VS AFTER REFERRAL PROGRAM
# -----------------------------------

print("\n--- BEFORE VS AFTER REFERRAL PROGRAM ---")

before_program = df_clean[
    df_clean["date"] < launch_date
]

after_program = df_clean[
    df_clean["date"] >= launch_date
]

print("\nBEFORE PROGRAM")
print("Transactions:", len(before_program))
print("Unique users:", before_program["user_id"].nunique())
print("Total money spent:", before_program["money_spent"].sum())
print("Average transaction:", before_program["money_spent"].mean())

print("\nAFTER PROGRAM")
print("Transactions:", len(after_program))
print("Unique users:", after_program["user_id"].nunique())
print("Total money spent:", after_program["money_spent"].sum())
print("Average transaction:", after_program["money_spent"].mean())

# -----------------------------------
# EXISTING VS NEW USERS AFTER LAUNCH
# -----------------------------------

print("\n--- EXISTING VS NEW USERS AFTER LAUNCH ---")

# Users observed before the referral program
before_users = set(before_program["user_id"].unique())

# Users observed after the referral program launched
after_users = set(after_program["user_id"].unique())

# Users appearing in both periods
existing_users = before_users.intersection(after_users)

# Users appearing only after launch
new_users = after_users - before_users

print("Users before launch:", len(before_users))
print("Users after launch:", len(after_users))
print("Existing users active after launch:", len(existing_users))
print("New users appearing after launch:", len(new_users))

# -----------------------------------
# NEW USERS AND REFERRAL ACTIVITY
# -----------------------------------

print("\n--- NEW USERS AND REFERRAL ACTIVITY ---")

new_user_transactions = after_program[
    after_program["user_id"].isin(new_users)
]

new_users_with_referral = (
    new_user_transactions[
        new_user_transactions["is_referral"] == 1
    ]["user_id"]
    .nunique()
)

new_users_without_referral = (
    new_user_transactions[
        new_user_transactions["is_referral"] == 0
    ]["user_id"]
    .nunique()
)

print("New users after launch:", len(new_users))
print("New users with referral activity:", new_users_with_referral)
print("New users with non-referral activity:", new_users_without_referral)

# -----------------------------------
# NEW USER REFERRAL BEHAVIOR
# -----------------------------------

print("\n--- NEW USER REFERRAL BEHAVIOR ---")

referral_users = set(
    new_user_transactions[
        new_user_transactions["is_referral"] == 1
    ]["user_id"].unique()
)

non_referral_users = set(
    new_user_transactions[
        new_user_transactions["is_referral"] == 0
    ]["user_id"].unique()
)

referral_only = referral_users - non_referral_users
non_referral_only = non_referral_users - referral_users
both = referral_users.intersection(non_referral_users)

print("Total new users:", len(new_users))
print("Referral only:", len(referral_only))
print("Non-referral only:", len(non_referral_only))
print("Both referral and non-referral:", len(both))

print(
    "Check total:",
    len(referral_only) +
    len(non_referral_only) +
    len(both)
)

# -----------------------------------
# NEW USER BUSINESS VALUE
# -----------------------------------

print("\n--- NEW USER BUSINESS VALUE ---")

groups = {
    "Referral Only": referral_only,
    "Non-Referral Only": non_referral_only,
    "Both": both
}

for group_name, user_group in groups.items():

    group_data = new_user_transactions[
        new_user_transactions["user_id"].isin(user_group)
    ]

    users = group_data["user_id"].nunique()
    transactions = len(group_data)
    total_spent = group_data["money_spent"].sum()
    avg_transaction = group_data["money_spent"].mean()
    avg_spent_per_user = total_spent / users

    print(f"\n{group_name}")
    print("Users:", users)
    print("Transactions:", transactions)
    print("Total money spent:", total_spent)
    print("Average transaction:", avg_transaction)
    print("Average spent per user:", avg_spent_per_user)

# -----------------------------------
# TRANSACTIONS PER NEW USER
# -----------------------------------

print("\n--- TRANSACTIONS PER NEW USER ---")

for group_name, user_group in groups.items():

    group_data = new_user_transactions[
        new_user_transactions["user_id"].isin(user_group)
    ]

    users = group_data["user_id"].nunique()
    transactions = len(group_data)

    transactions_per_user = transactions / users

    print(
        group_name,
        "- Average transactions per user:",
        transactions_per_user
    )

 # -----------------------------------
# GRAPH 1 - BEFORE VS AFTER PROGRAM
# -----------------------------------

periods = ["Before Program", "After Program"]

transactions = [
    len(before_program),
    len(after_program)
]

plt.figure(figsize=(8, 5))

bars = plt.bar(periods, transactions)

plt.title("Transactions Before vs After Referral Program")
plt.ylabel("Number of Transactions")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{int(bar.get_height()):,}",
        ha="center",
        va="bottom"
    )


plt.tight_layout()

plt.savefig(
    output_folder / "graph_01_before_after_transactions.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()   

# -----------------------------------
# GRAPH 2 - EXISTING VS NEW USERS
# -----------------------------------

user_types = ["Existing Users", "New Users"]

user_counts = [
    len(existing_users),
    len(new_users)
]

plt.figure(figsize=(8, 5))

bars = plt.bar(user_types, user_counts)

plt.title("Existing vs New Users After Referral Program Launch")
plt.ylabel("Number of Users")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{int(bar.get_height()):,}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(
    output_folder / "graph_02_existing_vs_new_users.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# -----------------------------------
# GRAPH 3 - NEW USER REFERRAL BEHAVIOR
# -----------------------------------

behavior_groups = [
    "Referral Only",
    "Non-Referral Only",
    "Both"
]

behavior_counts = [
    len(referral_only),
    len(non_referral_only),
    len(both)
]

plt.figure(figsize=(8, 5))

bars = plt.bar(behavior_groups, behavior_counts)

plt.title("New User Referral Behavior After Launch")
plt.ylabel("Number of New Users")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{int(bar.get_height()):,}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(
    output_folder / "graph_03_new_user_referral_behavior.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# -----------------------------------
# GRAPH 4 - TOTAL SPENDING BY GROUP
# -----------------------------------

spending_groups = [
    "Referral Only",
    "Non-Referral Only",
    "Both"
]

total_spending = []

for user_group in [referral_only, non_referral_only, both]:

    group_data = new_user_transactions[
        new_user_transactions["user_id"].isin(user_group)
    ]

    total_spending.append(
        group_data["money_spent"].sum()
    )

plt.figure(figsize=(8, 5))

bars = plt.bar(spending_groups, total_spending)

plt.title("Total Spending by New User Group")
plt.ylabel("Total Money Spent ($)")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"${bar.get_height():,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(
    output_folder / "graph_04_total_spending_by_group.png",
    dpi=300,
    bbox_inches="tight"
)   
plt.show()

# -----------------------------------
# GRAPH 5 - AVERAGE SPENDING PER USER
# -----------------------------------

avg_spending_per_user = []

for user_group in [referral_only, non_referral_only, both]:

    group_data = new_user_transactions[
        new_user_transactions["user_id"].isin(user_group)
    ]

    users = group_data["user_id"].nunique()
    total_spent = group_data["money_spent"].sum()

    avg_spending_per_user.append(
        total_spent / users
    )

plt.figure(figsize=(8, 5))

bars = plt.bar(
    spending_groups,
    avg_spending_per_user
)

plt.title("Average Spending per New User")
plt.ylabel("Average Spending per User ($)")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"${bar.get_height():,.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(
    output_folder / "graph_05_average_spending_per_user.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# -----------------------------------
# GRAPH 6 - TRANSACTIONS PER USER
# -----------------------------------

avg_transactions_per_user = []

for user_group in [referral_only, non_referral_only, both]:

    group_data = new_user_transactions[
        new_user_transactions["user_id"].isin(user_group)
    ]

    users = group_data["user_id"].nunique()
    transactions = len(group_data)

    avg_transactions_per_user.append(
        transactions / users
    )

plt.figure(figsize=(8, 5))

bars = plt.bar(
    spending_groups,
    avg_transactions_per_user
)

plt.title("Average Transactions per New User")
plt.ylabel("Average Transactions per User")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(
    output_folder / "graph_06_average_transactions_per_user.png",
    dpi=300,
    bbox_inches="tight"
)       
plt.show()

# -----------------------------------
# GRAPH 7 - DAILY TRANSACTION TREND
# -----------------------------------

daily_transactions = (
    df_clean
    .groupby("date")
    .size()
)

plt.figure(figsize=(12, 6))

plt.plot(
    daily_transactions.index,
    daily_transactions.values,
    marker="o"
)

# Mark referral program launch
plt.axvline(
    launch_date,
    linestyle="--",
    label="Referral Program Launch"
)

plt.title("Daily Transactions Before and After Referral Program Launch")
plt.xlabel("Date")
plt.ylabel("Number of Transactions")

plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.savefig(
    output_folder / "graph_07_daily_transactions.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# -----------------------------------
# GRAPH 8 - DAILY SPENDING TREND
# -----------------------------------

daily_spending = (
    df_clean
    .groupby("date")["money_spent"]
    .sum()
)

plt.figure(figsize=(12, 6))

plt.plot(
    daily_spending.index,
    daily_spending.values,
    marker="o"
)

plt.axvline(
    launch_date,
    linestyle="--",
    label="Referral Program Launch"
)

plt.title("Daily Spending Before and After Referral Program Launch")
plt.xlabel("Date")
plt.ylabel("Total Money Spent ($)")

plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.savefig(
    output_folder / "graph_08_daily_spending.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()  

# -----------------------------------
# GRAPH 9 - DAILY AVERAGE TRANSACTION
# -----------------------------------

daily_average_spending = (
    df_clean
    .groupby("date")["money_spent"]
    .mean()
)

plt.figure(figsize=(12, 6))

plt.plot(
    daily_average_spending.index,
    daily_average_spending.values,
    marker="o"
)

plt.axvline(
    launch_date,
    linestyle="--",
    label="Referral Program Launch"
)

plt.title("Daily Average Transaction Value Before and After Launch")
plt.xlabel("Date")
plt.ylabel("Average Transaction Value ($)")

plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.savefig(
    output_folder / "graph_09_daily_average_transaction.png",
    dpi=300,
    bbox_inches="tight"
)       
plt.show()

# -----------------------------------
# PREPARE EXISTING USER DAILY DATA
# -----------------------------------

existing_daily = (
    df_clean[
        df_clean["user_id"].isin(existing_users)
    ]
    .groupby("date")
    .agg(
        transactions=("user_id", "size"),
        active_users=("user_id", "nunique"),
        total_spent=("money_spent", "sum")
    )
)

existing_daily["transactions_per_active_user"] = (
    existing_daily["transactions"] /
    existing_daily["active_users"]
)
# -----------------------------------
# GRAPH 10 - EXISTING USER DAILY TRANSACTIONS
# -----------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    existing_daily.index,
    existing_daily["transactions"],
    marker="o"
)

plt.axvline(
    launch_date,
    linestyle="--",
    label="Referral Program Launch"
)

plt.title("Daily Transactions from Existing Users")
plt.xlabel("Date")
plt.ylabel("Number of Transactions")

plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()

plt.savefig(
    output_folder / "graph_10_existing_user_daily_transactions.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# -----------------------------------
# EXISTING USER BEFORE VS AFTER
# -----------------------------------

print("\n--- EXISTING USER BEFORE VS AFTER ---")

existing_before = before_program[
    before_program["user_id"].isin(existing_users)
]

existing_after = after_program[
    after_program["user_id"].isin(existing_users)
]

print("\nEXISTING USERS - BEFORE")
print("Users:", existing_before["user_id"].nunique())
print("Transactions:", len(existing_before))
print("Total money spent:", existing_before["money_spent"].sum())
print("Average transaction:", existing_before["money_spent"].mean())

print("\nEXISTING USERS - AFTER")
print("Users:", existing_after["user_id"].nunique())
print("Transactions:", len(existing_after))
print("Total money spent:", existing_after["money_spent"].sum())
print("Average transaction:", existing_after["money_spent"].mean())

before_transactions_per_user = (
    len(existing_before) /
    existing_before["user_id"].nunique()
)

after_transactions_per_user = (
    len(existing_after) /
    existing_after["user_id"].nunique()
)

print("\nAverage transactions per existing user:")
print("Before:", before_transactions_per_user)
print("After:", after_transactions_per_user)
print("\nAverage transactions per existing user:")

print("Before:", before_transactions_per_user)
print("After:", after_transactions_per_user)

print("\nEXISTING USERS - AFTER")
print("Users:", existing_after["user_id"].nunique())
print("Transactions:", len(existing_after))
print("Total money spent:", existing_after["money_spent"].sum())
print("Average transaction:", existing_after["money_spent"].mean())

before_transactions_per_user = (
    len(existing_before) /
    existing_before["user_id"].nunique()
)

after_transactions_per_user = (
    len(existing_after) /
    existing_after["user_id"].nunique()
)

print("\nAverage transactions per existing user:")
print("Before:", before_transactions_per_user)
print("After:", after_transactions_per_user)

# -----------------------------------
# EXISTING USER DAILY ACTIVITY
# -----------------------------------

print("\n--- EXISTING USER DAILY ACTIVITY ---")

existing_daily = (
    df_clean[
        df_clean["user_id"].isin(existing_users)
    ]
    .groupby("date")
    .agg(
        transactions=("user_id", "size"),
        active_users=("user_id", "nunique"),
        total_spent=("money_spent", "sum")
    )
)

existing_daily["transactions_per_active_user"] = (
    existing_daily["transactions"] /
    existing_daily["active_users"]
)

print(existing_daily)