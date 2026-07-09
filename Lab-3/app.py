import streamlit as st
import joblib

# Load the trained model
model = joblib.load('model.joblib')

st.title("News Article Categorizer")

# Text box for user input
article = st.text_area("Paste a news article here:")

if st.button("Predict Category"):
    if article.strip() == "":
        st.warning("Please enter some text first.")
    else:
        prediction = model.predict([article])[0]
        st.success(f"Predicted category: {prediction}")