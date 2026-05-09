# DuckDB Sales Analytics Application

## Project Overview
This project explores how DuckDB’s internal design supports analytical application behavior through a small sales analytics application. The project focuses on columnar storage and vectorized query execution, using grouped aggregation and filtering queries over supermarket sales data.

---

## Database System
This project uses **DuckDB** as the database system.

DuckDB is an in-process analytical database designed for **OLAP-style workloads**. It is well suited for scans, filters, projections, and grouped aggregations over structured tabular data. In this project, DuckDB is used to analyze supermarket sales data and to study how internal execution behavior maps to application operations.

---

## Folder Description
- `data/` contains the dataset and DuckDB database file
- `documents/` contains the proposal, reports, and demo slides
- `source_code/` contains the notebook implementation and the Streamlit application
- `README.md` provides setup and usage instructions
- `requirements.txt` lists the Python dependencies

---

## Requirements
- Python 3.x
- DuckDB
- pandas
- streamlit
- matplotlib
- jupyter

---

## Installation
Install dependencies with:

```bash
py -m pip install -r requirements.txt
```

---

## Main Features
The application supports the following analytical operations:

1. **Total sales by city**  
   Computes total sales for each city.

2. **Sales in a date range**  
   Computes total sales within a selected time window.

3. **Average sales by product line**  
   Compares product categories by average sales.

4. **Payment summary**  
   Computes transaction count and total sales by payment method.

5. **Branch-product summary**  
   Computes total sales by branch and product line.

The project also includes:

- `EXPLAIN` and `EXPLAIN ANALYZE` for query-plan inspection
- lightweight runtime validation on scaled datasets
- a notebook implementation and a simple Streamlit application UI

---

## Dataset
The dataset used in this project is included in the data/ folder:
- SuperMarket Analysis.csv
- supermarket.duckdb
The CSV file is the original dataset, and the .duckdb file is included for convenience.

---

## Secret Keys / Credentials
This project does not require API keys, tokens, or external credentials.

---

## How to Run the Notebook
From the project directory, open: source_code/551project.ipynb
Run the notebook cells in order to:
- load the dataset,
- create the DuckDB table,
- execute analytical queries,
- inspect query plans with EXPLAIN,
- run lightweight validation experiments.

---

## How to Run the Streamlit Application
From the project root directory, run:
```bash
py -m streamlit run "source_code/app.py"
```
If needed, you can also change into the source_code/ directory first:
```bash
cd source_code
py -m streamlit run app.py
```

---

## How to Reproduce Main Results

To reproduce the main results:
- Use the notebook or Streamlit app
- Run the analytical operations: total sales by city, sales in a date range, average sales by product line, payment summary, and branch-product summary
- Use EXPLAIN and EXPLAIN ANALYZE to inspect query behavior
- Review the scaled-data runtime experiments included in the notebook


