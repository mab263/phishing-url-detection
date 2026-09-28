import pandas as pd

# Load the dataset
df = pd.read_csv("data/phishing_urls.csv")

# Basic checks
print(df.shape)          # rows, columns
print(df.head())         # first 5 rows
print(df.columns)        # column names
print(df.isnull().sum()) # missing values per column