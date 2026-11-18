from src.data_cleaning import clean_data

# Step 1: Clean data (this creates df)
df = clean_data("data/raw/netflix_titles.csv")

# Step 2: Print output
print(df.head())
print(df.info())