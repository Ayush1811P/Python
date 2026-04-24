import pandas as pd
from sqlalchemy import create_engine

# Load datasets
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

# Merge datasets
df = pd.merge(deliveries, matches, left_on='match_id', right_on='id')

# Cleaning
df['winner'].fillna("No Result", inplace=True)
df['date'] = pd.to_datetime(df['date'])

# Save cleaned file
df.to_csv("data/cleaned_ipl.csv", index=False)

# Store to MySQL
engine = create_engine("mysql+pymysql://root:88008191@localhost/ipl_analysis")
df.to_sql("ipl_data", con=engine, if_exists="replace", index=False)

print("Pipeline completed successfully!")
