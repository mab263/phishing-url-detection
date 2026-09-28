import pandas as pd

# Load the dataset
df = pd.read_csv("data/phishing_urls.csv")

# Basic checks
print(df.shape)          # rows, columns
print(df.head())         # first 5 rows
print(df.columns)        # column names
print(df.isnull().sum()) # missing values per column

# Check class balance
print(df['target'].value_counts())
print(df['target'].value_counts(normalize=True))  # as percentages

# Correlation of each feature with target
correlations = df.corr(numeric_only=True)['target'].sort_values(ascending=False)
print(correlations)

# For good measure: look at raw URL examples for each class (if a url text column exists)
# If there isn't one, check what a known phishing-style row looks like:
print(df[df['target'] == 1][['url_length', 'isHttps', 'valid_url', 'nb_www']].describe())
print(df[df['target'] == 0][['url_length', 'isHttps', 'valid_url', 'nb_www']].describe())