import pandas as pd 
from pathlib import Path

# Find the CSV in the other data folder
data_path = Path(__file__).resolve().parent.parent / "data" / "sales_data.csv"
df = pd.read_csv(data_path)

#Convert dates
df["date"] = pd.to_datetime(df["date"], errors="coerce")

print("Accuracy Check")

negative_prices = (df["price"] < 0).sum()
print(f"Negative Prices: {negative_prices}")

today = pd.Timestamp.today().normalize()
future_date_count = (df["date"] > today).sum()
print(f"Number of Future Dates: {future_date_count}")

print("\nConsistency Check")

unique_products = df["product"].unique()
unique_count = df["product"].nunique()

print(f"Unique products: {unique_products}")
print(f"Count of unique products: {unique_count}")

print("\nCompleteness Check")

missing_values = df.isna().sum()
completeness = df.notna().sum().sum() / df.size * 100

print(f"Missing Values: {missing_values}")
print(f"Overall completeness rate: {completeness:.1f}%")

assert not (df["price"] < 0).any(), "Negative prices are not allowed."

