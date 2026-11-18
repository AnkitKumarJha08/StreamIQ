import streamlit as st
import requests

BACKEND = "http://127.0.0.1:8000"

st.set_page_config(layout="wide")

# 🎬 TITLE
st.markdown("<h1 style='text-align:center;'>🎬 StreamIQ</h1>", unsafe_allow_html=True)

# 🔍 SEARCH
query = st.text_input("🔍 Search Movies")

# 🧠 MOOD SELECTOR
st.markdown("## 🧠 Mood Based Search")
mood = st.selectbox("Select Mood", ["romantic", "adventure", "thriller", "comedy", "horror", "happy", "sad"])

# 🔥 SEARCH BUTTON
if st.button("Search"):
    try:
        res = requests.get(f"{BACKEND}/movies/search/{query}").json()

        st.markdown("## 🎯 Results")

        if len(res) == 0:
            st.warning("No movies found ❌")
        else:
            cols = st.columns(5)

            for i, m in enumerate(res[:10]):
                with cols[i % 5]:
                    if m["Poster"] != "N/A":
                        st.image(m["Poster"], use_column_width=True)
                    st.write(f"🎬 {m['Title']}")
                    st.caption(f"📅 {m['Year']}")

    except:
        st.error("Error ❌")

# 🧠 MOOD BUTTON
st.markdown("## 🧠 AI Mood Search")

mood_input = st.text_input("Describe your mood (e.g. sad, romantic, bored)")

if st.button("Get AI Recommendations"):
    try:
        res = requests.get(f"{BACKEND}/ai/mood/{mood_input}").json()

        st.markdown("## 🎬 Recommended for You")

        if len(res) == 0:
            st.warning("No results found ❌")
        else:
            cols = st.columns(5)

            for i, m in enumerate(res):
                with cols[i % 5]:
                    if m["Poster"] != "N/A":
                        st.image(m["Poster"], use_column_width=True)
                    st.write(m["Title"])
                    st.caption(m["Year"])

    except:
        st.error("Server error ❌")