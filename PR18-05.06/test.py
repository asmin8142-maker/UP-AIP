import pandas as pd

df = pd.read_csv(
    "data/dataset.csv",
    skiprows=2
)

print(df.columns)
print(df.head())