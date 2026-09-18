"""
app.py
------
Streamlit dashboard. Run with: streamlit run app.py

Logic:
1. Let the user upload a CSV (or default to sample_transactions.csv).
2. Run it through clean_pipeline -> categorize_all.
3. Show key stats at the top (total spent, avg daily, biggest expense).
4. Show a bar chart of spend_by_category.
5. Show a line chart of spend_by_month.
6. Show the predicted next month spend by category.
7. Show the raw categorized table at the bottom (so user can sanity-check
   categorization and spot "Uncategorized" rows to fix).
"""

import streamlit as st
import pandas as pd

from clean import clean_pipeline
from categorize import categorize_all
from analyze import spend_by_category, spend_by_month, key_stats
from predict import predict_next_month

st.title("Personal Expense Tracker")

uploaded = st.file_uploader("Upload your transactions CSV", type="csv")
csv_path = uploaded if uploaded else "../data/sample_transactions.csv"

# NOTE: clean_pipeline expects a path; if using an uploaded file object,
# you'll need to adapt load_transactions() to accept a file-like object too
# (pd.read_csv handles both a path string and an uploaded file object the same way).
df = clean_pipeline(csv_path)
df = categorize_all(df)

stats = key_stats(df)
col1, col2, col3 = st.columns(3)
col1.metric("Total Spent", f"${stats.get('total_spent', 0):,.2f}")
col2.metric("Avg Daily Spend", f"${stats.get('avg_daily_spend', 0):,.2f}")
col3.metric("MoM Change", f"{stats.get('mom_change', 0):.1f}%")

st.subheader("Spend by Category")
st.bar_chart(spend_by_category(df))

st.subheader("Spend Over Time")
st.line_chart(spend_by_month(df))

st.subheader("Predicted Next Month")
st.write(predict_next_month(df))

st.subheader("All Transactions")
st.dataframe(df)
