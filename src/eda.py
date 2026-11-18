import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from collections import Counter

# Load data
df = pd.read_csv("data/processed/cleaned_netflix_data.csv")


# 🎯 Recommendation system
def recommend_by_genre(df, genre):
    return df[df['main_genre'] == genre][['title', 'type']].head(10)


# 📈 Growth prediction
def predict_growth(df):
    year_data = df['year_added'].value_counts().sort_index()

    X = np.array(year_data.index).reshape(-1, 1)
    y = year_data.values

    model = LinearRegression()
    model.fit(X, y)

    future_years = np.array([[2023], [2024], [2025]])
    predictions = model.predict(future_years)

    return predictions


# 🎭 Top actors
def top_actors(df):
    actors = df['cast'].dropna().str.split(', ')
    all_actors = [actor for sublist in actors for actor in sublist]

    return Counter(all_actors).most_common(10)


# 🔥 TEST OUTPUT
if __name__ == "__main__":
    print("🎯 Recommendations (Drama):")
    print(recommend_by_genre(df, "Dramas"))

    print("\n📈 Future Growth:")
    print(predict_growth(df))

    print("\n🎭 Top Actors:")
    print(top_actors(df))