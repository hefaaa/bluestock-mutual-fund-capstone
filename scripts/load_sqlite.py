import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# Create SQLite Database
# -----------------------------
engine = create_engine("sqlite:///db/bluestock_mf.db")

print("Creating SQLite database...\n")

# -----------------------------
# Load datasets
# -----------------------------

# Raw datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category = pd.read_csv("data/raw/05_category_inflows.csv")
folio = pd.read_csv("data/raw/06_industry_folio_count.csv")
holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

# Cleaned datasets
nav = pd.read_csv("data/processed/nav_history_clean.csv")
transactions = pd.read_csv("data/processed/investor_transactions_clean.csv")
performance = pd.read_csv("data/processed/scheme_performance_clean.csv")

print("Datasets loaded successfully.\n")

# -----------------------------
# Save to SQLite
# -----------------------------

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

sip.to_sql(
    "monthly_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)

category.to_sql(
    "category_inflows",
    engine,
    if_exists="replace",
    index=False
)

folio.to_sql(
    "industry_folio_count",
    engine,
    if_exists="replace",
    index=False
)

holdings.to_sql(
    "portfolio_holdings",
    engine,
    if_exists="replace",
    index=False
)

benchmark.to_sql(
    "benchmark_indices",
    engine,
    if_exists="replace",
    index=False
)

print("All datasets loaded into SQLite successfully!\n")

# -----------------------------
# Verify row counts
# -----------------------------

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum",
    "monthly_sip_inflows",
    "category_inflows",
    "industry_folio_count",
    "portfolio_holdings",
    "benchmark_indices"
]

print("Row Counts")
print("-" * 40)

for table in tables:
    query = f"SELECT COUNT(*) AS rows FROM {table}"
    rows = pd.read_sql(query, engine)

    print(f"{table:25} {rows.iloc[0,0]}")

print("\nDatabase loading completed successfully!")