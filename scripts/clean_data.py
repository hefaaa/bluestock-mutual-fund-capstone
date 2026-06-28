import pandas as pd

print("Cleaning nav_history...")

# load
nav = pd.read_csv("data/raw/02_nav_history.csv")

# clean
nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

# save
nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Done!")
print("Cleaning investor_transactions...")
print("Cleaning scheme_performance...")

print("\nCleaning investor_transactions.csv...")

# Load dataset
txn = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert transaction date to datetime
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

# Standardize transaction types
txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

# Convert "Sip" back to "SIP"
txn["transaction_type"] = txn["transaction_type"].replace({
    "Sip": "SIP"
})

# Keep only positive transaction amounts
txn = txn[txn["amount_inr"] > 0]

# Check KYC values
print("\nKYC Status Values:")
print(txn["kyc_status"].unique())

# Save cleaned dataset
txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("investor_transactions.csv cleaned successfully!")

print("\nCleaning scheme_performance.csv...")

# Load dataset
perf = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

# Find rows with missing numeric values
anomalies = perf[perf[return_cols].isnull().any(axis=1)]

print("\nRows with numeric anomalies:")
print(len(anomalies))

# Check expense ratio range
invalid_expense = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

print("Funds with invalid expense ratio:")
print(len(invalid_expense))

# Save cleaned dataset
perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("scheme_performance.csv cleaned successfully!")