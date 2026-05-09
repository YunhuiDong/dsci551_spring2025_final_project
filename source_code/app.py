from pathlib import Path
import streamlit as st
import duckdb
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR.parent / "data" / "supermarket.duckdb"

st.set_page_config(page_title="DuckDB Sales Analytics", layout="wide")

st.title("DuckDB Sales Analytics Application")
st.write("This application demonstrates analytical queries in DuckDB using supermarket sales data.")

@st.cache_resource
def get_connection():
    try:
        return duckdb.connect(str(DB_PATH))
    except Exception as e:
        st.error(f"Failed to connect to DuckDB database: {e}")
        st.stop()

con = get_connection()

operation = st.sidebar.selectbox(
    "Choose an operation",
    [
        "Total sales by city",
        "Sales in a date range",
        "Average sales by product line",
        "Payment summary",
        "Branch-product summary"
    ]
)

st.subheader("Selected Operation")
st.write(operation)

if operation == "Total sales by city":
    st.markdown("**What the application does:** Computes total sales for each city.")
    st.markdown("**What the database does internally:** Reads `city` and `sales`, then performs grouped aggregation.")
    st.markdown("**Why it matters:** Shows how DuckDB supports analytical aggregation efficiently.")

    query = """
    SELECT city, SUM(sales) AS total_sales
    FROM supermarket_sales
    GROUP BY city
    ORDER BY total_sales DESC
    """
    df = con.execute(query).df()
    st.dataframe(df, use_container_width=True)

    if st.button("Show EXPLAIN Plan", key="explain_city"):
        plan = con.execute(f"EXPLAIN {query}").fetchone()[1]
        st.text(plan)

elif operation == "Sales in a date range":
    st.markdown("**What the application does:** Computes sales in a selected time range.")
    st.markdown("**What the database does internally:** Filters on `sale_date` and aggregates `sales`.")
    st.markdown("**Why it matters:** Shows how filtering and aggregation support reporting workloads.")

    start_date = st.date_input("Start date", value=pd.to_datetime("2019-01-01"))
    end_date = st.date_input("End date", value=pd.to_datetime("2019-01-31"))

    if start_date > end_date:
        st.error("Start date must be earlier than or equal to end date.")
    else:
        query = f"""
        SELECT SUM(sales) AS total_sales
        FROM supermarket_sales
        WHERE sale_date BETWEEN DATE '{start_date}' AND DATE '{end_date}'
        """
        df = con.execute(query).df()
        st.dataframe(df, use_container_width=True)

        if st.button("Show EXPLAIN Plan", key="explain_date"):
            plan = con.execute(f"EXPLAIN {query}").fetchone()[1]
            st.text(plan)

elif operation == "Average sales by product line":
    st.markdown("**What the application does:** Compares product categories by average sales.")
    st.markdown("**What the database does internally:** Groups by `product_line` and aggregates `sales`.")
    st.markdown("**Why it matters:** Shows another analytical query pattern supported by DuckDB.")

    query = """
    SELECT product_line, AVG(sales) AS avg_sales
    FROM supermarket_sales
    GROUP BY product_line
    ORDER BY avg_sales DESC
    """
    df = con.execute(query).df()
    st.dataframe(df, use_container_width=True)

    if st.button("Show EXPLAIN Plan", key="explain_product"):
        plan = con.execute(f"EXPLAIN {query}").fetchone()[1]
        st.text(plan)

elif operation == "Payment summary":
    query = """
    SELECT payment, COUNT(*) AS num_transactions, SUM(sales) AS total_sales
    FROM supermarket_sales
    GROUP BY payment
    ORDER BY total_sales DESC
    """
    df = con.execute(query).df()
    st.dataframe(df, use_container_width=True)

    if st.button("Show EXPLAIN Plan", key="explain_payment"):
        plan = con.execute(f"EXPLAIN {query}").fetchone()[1]
        st.text(plan)

elif operation == "Branch-product summary":
    query = """
    SELECT branch, product_line, SUM(sales) AS total_sales
    FROM supermarket_sales
    GROUP BY branch, product_line
    ORDER BY branch, total_sales DESC
    """
    df = con.execute(query).df()
    st.dataframe(df, use_container_width=True)

    if st.button("Show EXPLAIN Plan", key="explain_branch"):
        plan = con.execute(f"EXPLAIN {query}").fetchone()[1]
        st.text(plan)

st.markdown("""
---
### Validation Summary
- Used `EXPLAIN` and `EXPLAIN ANALYZE` to inspect query behavior
- Compared average runtime on scaled datasets
- Focused on aggregation and filtering as analytical operations
""")