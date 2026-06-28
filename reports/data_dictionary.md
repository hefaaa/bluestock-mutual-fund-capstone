# Data Dictionary

---

# dim_fund

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| amfi_code | INTEGER | Unique AMFI scheme code | fund_master.csv |
| fund_house | TEXT | Mutual fund company | fund_master.csv |
| scheme_name | TEXT | Mutual fund scheme name | fund_master.csv |
| category | TEXT | Fund category | fund_master.csv |
| sub_category | TEXT | Fund sub-category | fund_master.csv |
| plan | TEXT | Direct/Regular plan | fund_master.csv |
| launch_date | DATE | Scheme launch date | fund_master.csv |
| benchmark | TEXT | Benchmark index | fund_master.csv |
| expense_ratio_pct | REAL | Expense ratio (%) | fund_master.csv |
| exit_load_pct | REAL | Exit load (%) | fund_master.csv |
| fund_manager | TEXT | Fund manager | fund_master.csv |
| risk_category | TEXT | Risk classification | fund_master.csv |
| sebi_category_code | TEXT | SEBI category code | fund_master.csv |

---

# fact_nav

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| amfi_code | INTEGER | Mutual fund scheme code | nav_history.csv |
| date | DATE | NAV date | nav_history.csv |
| nav | REAL | Net Asset Value | nav_history.csv |

---

# fact_transactions

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| investor_id | TEXT | Investor ID | investor_transactions.csv |
| transaction_date | DATE | Transaction date | investor_transactions.csv |
| amfi_code | INTEGER | Fund scheme | investor_transactions.csv |
| transaction_type | TEXT | SIP/Lumpsum/Redemption | investor_transactions.csv |
| amount_inr | REAL | Investment amount | investor_transactions.csv |
| state | TEXT | Investor state | investor_transactions.csv |
| city | TEXT | Investor city | investor_transactions.csv |
| city_tier | TEXT | City classification | investor_transactions.csv |
| age_group | TEXT | Investor age group | investor_transactions.csv |
| gender | TEXT | Investor gender | investor_transactions.csv |
| annual_income_lakh | REAL | Annual income | investor_transactions.csv |
| payment_mode | TEXT | Payment method | investor_transactions.csv |
| kyc_status | TEXT | KYC verification status | investor_transactions.csv |

---

# fact_performance

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| amfi_code | INTEGER | Scheme code | scheme_performance.csv |
| return_1yr_pct | REAL | 1-year return (%) | scheme_performance.csv |
| return_3yr_pct | REAL | 3-year return (%) | scheme_performance.csv |
| return_5yr_pct | REAL | 5-year return (%) | scheme_performance.csv |
| benchmark_3yr_pct | REAL | Benchmark return | scheme_performance.csv |
| alpha | REAL | Alpha | scheme_performance.csv |
| beta | REAL | Beta | scheme_performance.csv |
| sharpe_ratio | REAL | Sharpe Ratio | scheme_performance.csv |
| sortino_ratio | REAL | Sortino Ratio | scheme_performance.csv |
| std_dev_ann_pct | REAL | Annualized standard deviation | scheme_performance.csv |
| max_drawdown_pct | REAL | Maximum drawdown | scheme_performance.csv |
| expense_ratio_pct | REAL | Expense ratio | scheme_performance.csv |
| morningstar_rating | INTEGER | Morningstar rating | scheme_performance.csv |
| risk_grade | TEXT | Risk grade | scheme_performance.csv |

---

# fact_aum

| Column | Data Type | Description | Source |
|----------|-----------|-------------|--------|
| date | DATE | Reporting date | aum_by_fund_house.csv |
| fund_house | TEXT | Fund house | aum_by_fund_house.csv |
| aum_lakh_crore | REAL | AUM (Lakh Crore) | aum_by_fund_house.csv |
| aum_crore | REAL | AUM (Crore) | aum_by_fund_house.csv |
| num_schemes | INTEGER | Number of schemes | aum_by_fund_house.csv |