import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")

csv_files = sorted(raw_path.glob("*.csv"))

for file in csv_files:
    print("\n" + "="*50)
    print(file.name)

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicates:")
    print(df.duplicated().sum())

    print("\nHead:")
    print(df.head())