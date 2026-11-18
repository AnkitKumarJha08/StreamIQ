import pandas as pd
import os

# Create folder
os.makedirs("data/raw", exist_ok=True)

# ✅ Correct dataset URL
url = "https://raw.githubusercontent.com/mk-gurucharan/Regression-Data/master/Netflix%20Dataset.csv"

# Download
df = pd.read_csv(url)

# Save
df.to_csv("data/raw/netflix_titles.csv", index=False)

print("✅ Dataset downloaded successfully!")