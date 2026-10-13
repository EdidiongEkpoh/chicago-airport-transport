CREATE CATALOG IF NOT exists airport 
COMMENT 'Chicago airport ground transport & weather project';

CREATE SCHEMA IF NOT EXISTS airport.bronze COMMENT 'Raw data as ingested';
CREATE SCHEMA IF NOT EXISTS airport.silver COMMENT 'Formatted and validated; timestamps in America/Chicago + UTC';
CREATE SCHEMA IF NOT EXISTS airport.gold COMMENT 'star schema; hourly and weekly airport marts';
CREATE SCHEMA IF NOT EXISTS airport.ml COMMENT 'Winter outlook features, scenarios, and backtest outputs';

CREATE VOLUME IF NOT EXISTS airport.bronze.landing 
COMMENT 'Raw downloaded files, partitioned by source and month';

CREATE VOLUME IF NOT EXISTS airport.gold.exports 
COMMENT 'BI-ready CSV extracts written by a scheduled job';

SHOW SCHEMAS IN airport;
SHOW VOLUMES IN airport.bronze;