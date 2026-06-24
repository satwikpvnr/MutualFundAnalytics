-- Total NAV records
SELECT COUNT(*) FROM fact_nav;

-- Total Transactions
SELECT COUNT(*) FROM fact_transactions;

-- Total Performance Records
SELECT COUNT(*) FROM fact_performance;

-- Transaction Type Count
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- KYC Status Count
SELECT kyc_status, COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;