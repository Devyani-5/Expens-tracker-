"""
analyze.py
----------
Logic:
1. spend_by_category:
   - Filter to expenses only (amount < 0)
   - Group by 'category', sum the amounts
   - Take absolute value (so it reads as positive spend)
   - Sort descending -> biggest spending categories first

2. spend_by_month:
   - Create a 'month' column from date (df['date'].dt.to_period('M'))
   - Group by 'month', sum amounts (expenses only)
   - Sort chronologically

3. key_stats:
   - total_spent = sum of all expense amounts (abs value)
   - avg_daily_spend = total_spent / number of unique days in the data
   - biggest_expense = the single largest transaction (most negative amount)
   - month_over_month_change = % change between last two months in spend_by_month
"""

import pandas as pd


def spend_by_category(df: pd.DataFrame) -> pd.Series:
    # expenses = df[df['amount'] < 0]
    # grouped = expenses.groupby('category')['amount'].sum().abs()
    # return grouped.sort_values(ascending=False)
    pass


def spend_by_month(df: pd.DataFrame) -> pd.Series:
    # df['month'] = df['date'].dt.to_period('M')
    # expenses = df[df['amount'] < 0]
    # grouped = expenses.groupby('month')['amount'].sum().abs()
    # return grouped.sort_index()
    pass


def key_stats(df: pd.DataFrame) -> dict:
    # total_spent = df[df['amount'] < 0]['amount'].sum() * -1
    # num_days = df['date'].dt.date.nunique()
    # avg_daily_spend = total_spent / num_days
    # biggest_expense = df.loc[df['amount'].idxmin()]  # most negative row
    # monthly = spend_by_month(df)
    # mom_change = (monthly.iloc[-1] - monthly.iloc[-2]) / monthly.iloc[-2] * 100
    # return dict with all of the above
    pass


if __name__ == "__main__":
    from clean import clean_pipeline
    from categorize import categorize_all

    df = clean_pipeline("../data/sample_transactions.csv")
    df = categorize_all(df)

    print("Spend by category:")
    print(spend_by_category(df))

    print("\nSpend by month:")
    print(spend_by_month(df))

    print("\nKey stats:")
    print(key_stats(df))
