"""
predict.py
----------
Logic (simple version — good enough to talk about in an interview):
1. Take spend_by_category grouped ALSO by month (category x month table).
   Use df.pivot_table(index='month', columns='category', values='amount',
   aggfunc=lambda x: x.sum() * -1, fill_value=0)
2. For each category, average the last 3 months (or all available months
   if fewer than 3).
3. Return a dict: {category: predicted_next_month_spend}

Stretch goal (mention this in your resume bullet even if you only partly
implement it): swap the average for a linear regression per category
(from sklearn.linear_model import LinearRegression) using month index as
X and spend as y, then predict the next index. This is what turns "did a
tutorial project" into "applied a forecasting model" on your resume.
"""

import pandas as pd


def build_monthly_category_table(df: pd.DataFrame) -> pd.DataFrame:
    # df['month'] = df['date'].dt.to_period('M')
    # pivot = df.pivot_table(index='month', columns='category', values='amount',
    #                         aggfunc=lambda x: x.sum() * -1, fill_value=0)
    # return pivot
    pass


def predict_next_month(df: pd.DataFrame, lookback_months: int = 3) -> dict:
    # pivot = build_monthly_category_table(df)
    # recent = pivot.tail(lookback_months)
    # predictions = recent.mean().to_dict()
    # return predictions
    pass


if __name__ == "__main__":
    from clean import clean_pipeline
    from categorize import categorize_all

    df = clean_pipeline("../data/sample_transactions.csv")
    df = categorize_all(df)

    print("Predicted next month spend by category:")
    for category, amount in predict_next_month(df).items():
        print(f"  {category}: ${amount:.2f}")
