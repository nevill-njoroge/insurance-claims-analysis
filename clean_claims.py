import pandas as pd

# Load data
df = pd.read_csv('claims.csv')

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Fill missing values
df['claim_amount'] = df['claim_amount'].fillna(df['claim_amount'].median())
df['age'] = df['age'].fillna(df['age'].median())

# 3. Calculate loss ratio
df['loss_ratio'] = df['claim_amount'] / df['premium']

# 4. Summary by policy type
summary = df.groupby('policy_type')['loss_ratio'].mean()

print(summary)
df.to_csv('claims_cleaned.csv', index=False)
print("Cleaned:", len(df), "records")