SELECT fund_house,
aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

SELECT fund_house,
       aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
strftime('%Y-%m', date) AS Month,
AVG(nav) AS Average_NAV
FROM fact_nav
GROUP BY Month
ORDER BY Month;

SELECT
strftime('%Y-%m', date) AS Month,
AVG(nav) AS Average_NAV
FROM fact_nav
GROUP BY Month
ORDER BY Month;

