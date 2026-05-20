from pathlib import Path
import pandas as pd



input = Path("data/team_2.parquet")
output = Path("output/partitioned_dataset")


df = pd.read_parquet(input)

print("\nDataset loaded successfully.")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nColumns:")
print(df.columns.tolist())

print("\nPreview:")
print(df.head())


# =========================================================
# FIND DATE COLUMN
# =========================================================

date_column = "timestamp"

# =========================================================
# CONVERT TO DATETIME
# =========================================================

df[date_column] = pd.to_datetime(df[date_column])

# =========================================================
# CREATE PARTITION COLUMNS
# =========================================================

df["year"] = df[date_column].dt.year
df["month"] = df[date_column].dt.month
df["day"] = df[date_column].dt.day


# =========================================================
# WRITE PARTITIONED DATASET
# =========================================================

print("\nWriting partitioned parquet dataset...")

df.to_parquet(
    output,
    engine="pyarrow",
    partition_cols=["year", "month", "day"],
    index=False
)

print(f"Partitioned dataset written to: {output.resolve()}")