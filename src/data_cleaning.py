import pandas as pd

def clean_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # -------------------------------
    # Handle Missing Values
    # -------------------------------
    df['country'] = df['country'].fillna('Unknown')
    df['director'] = df['director'].fillna('Not Available')
    df['cast'] = df['cast'].fillna('Not Available')

    # -------------------------------
    # Convert Date Column
    # -------------------------------
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Extract year & month
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month

    # -------------------------------
    # Clean Duration Column
    # -------------------------------
    df['duration'] = df['duration'].astype(str)

    # Separate duration into numeric + type
    df['duration_int'] = df['duration'].str.extract(r'(\d+)').astype(float)
    df['duration_type'] = df['duration'].str.replace(r'\d+', '', regex=True).str.strip()
    # -------------------------------
    # Clean Genre Column
    # -------------------------------
    df['listed_in'] = df['listed_in'].fillna('Unknown')

    # Keep first genre for simplicity
    df['main_genre'] = df['listed_in'].apply(lambda x: x.split(',')[0])

    # -------------------------------
    # Remove duplicates
    # -------------------------------
    df.drop_duplicates(inplace=True)

    # -------------------------------
    # Save cleaned data
    # -------------------------------
    df.to_csv("data/processed/cleaned_netflix_data.csv", index=False)

    print("✅ Data cleaned and saved successfully!")

    return df