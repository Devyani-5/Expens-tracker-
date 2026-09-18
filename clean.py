"""
clean.py
--------
Logic:
1. Load the raw CSV into a DataFrame.
2. Parse the date column into real datetime objects (so we can group by month later).
3. Drop exact duplicate rows (some bank exports repeat pending transactions).
4. Strip extra whitespace / uppercase junk from the description field.
5. Make sure amount is numeric (in case it was exported as a string like "$12.34").
6. Return a clean DataFrame with columns: date, description, amount.

Fill in each function body yourself — the comments describe exactly what
each line should do. This is intentional: writing this out is where the
actual learning (and resume-worthy skill) happens.
"""

import pandas as pd


def load_transactions(csv_path: str) -> pd.DataFrame:
    # 1. pd.read_csv(csv_path)
    # 2. convert the 'date' column to datetime with pd.to_datetime()
    # 3. return the dataframe
    pass


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    # df.drop_duplicates() -- consider subset=['date','description','amount']
    pass


def clean_descriptions(df: pd.DataFrame) -> pd.DataFrame:
    # df['description'] = df['description'].str.strip().str.upper()
    # (uppercasing makes keyword matching in categorize.py case-insensitive-safe)
    pass


def clean_amounts(df: pd.DataFrame) -> pd.DataFrame:
    # if amount column is not numeric, use pd.to_numeric(df['amount'], errors='coerce')
    # then drop rows where amount is NaN (couldn't be parsed)
    pass


def clean_pipeline(csv_path: str) -> pd.DataFrame:
    """Run the full cleaning pipeline and return a ready-to-use DataFrame."""
    df = load_transactions(csv_path)
    df = drop_duplicates(df)
    df = clean_descriptions(df)
    df = clean_amounts(df)
    return df


if __name__ == "__main__":
    df = clean_pipeline("../data/sample_transactions.csv")
    print(df.head())
