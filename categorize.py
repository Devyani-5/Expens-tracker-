"""
categorize.py
--------------
Logic:
1. Define a dictionary mapping keywords -> category.
   e.g. {"STARBUCKS": "Coffee", "UBER": "Transport", "WHOLE FOODS": "Groceries"}
2. For each transaction description, loop through the keyword dict.
3. If a keyword is found inside the description (substring match), assign
   that category.
4. If no keyword matches, assign "Uncategorized" so you can review and
   expand your keyword dict later.
5. Add the result as a new 'category' column on the DataFrame.
"""

import pandas as pd

KEYWORD_MAP = {
    "STARBUCKS": "Coffee",
    "UBER EATS": "Food Delivery",
    "UBER": "Transport",
    "WHOLE FOODS": "Groceries",
    "TRADER JOES": "Groceries",
    "TARGET": "Shopping",
    "AMAZON": "Shopping",
    "NETFLIX": "Subscriptions",
    "SPOTIFY": "Subscriptions",
    "GYM": "Health",
    "SHELL": "Gas",
    "PAYCHECK": "Income",
}


def categorize_transaction(description: str, keyword_map: dict = KEYWORD_MAP) -> str:
    # loop through keyword_map.items()
    # if keyword in description: return category
    # if nothing matches after the loop: return "Uncategorized"
    pass


def categorize_all(df: pd.DataFrame) -> pd.DataFrame:
    # df['category'] = df['description'].apply(categorize_transaction)
    # return df
    pass


if __name__ == "__main__":
    from clean import clean_pipeline

    df = clean_pipeline("../data/sample_transactions.csv")
    df = categorize_all(df)
    print(df.head(10))
    print("\nUncategorized rows to review:")
    print(df[df["category"] == "Uncategorized"])
