import streamlit as st
import joblib
import numpy as np
import os

# Load model safely
MODEL_PATH = os.path.join("assets", "model.pkl")

try:
    with open(MODEL_PATH, "rb") as f:
        model = joblib.load(f)
except FileNotFoundError:
    st.error(f"❌ Model file not found at {MODEL_PATH}. Please make sure it exists.")
    st.stop()

# --- Page Config ---
st.set_page_config(page_title="🏡 House Price Prediction", page_icon=":house:", layout="centered")

# --- Custom CSS for Pastel Theme ---
st.markdown(
    """
    <style>
    /* Page background */
    .stApp {
        background-color: #fdf6f0; /* soft peach */
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Titles */
    h1, h2, h3 {
        color: #6a5acd; /* pastel purple */
        font-weight: bold;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #f0f8ff; /* pastel blue */
        border-radius: 10px;
        padding: 15px;
    }

    /* Buttons */
    .stButton > button {
        background-color: #ffb6b9; /* pastel pink */
        color: white;
        border-radius: 10px;
        height: 3em;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #ff929c; /* darker pink */
    }

    /* Success box */
    .stSuccess {
        background-color: #d1f7d6 !important; /* pastel green */
        color: #333333 !important;
        border-radius: 10px;
    }

    /* Footer text */
    .footer {
        text-align: center;
        font-size: 14px;
        margin-top: 30px;
        color: #555555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Main Content ---
st.title("🏡 House Price Prediction App")
st.write("Welcome to your modern, pastel-themed prediction app ✨")

# Sidebar inputs
st.sidebar.header("Enter House Details")

bedrooms = st.sidebar.slider("Bedrooms", 1, 10, 3)
bathrooms = st.sidebar.slider("Bathrooms", 1, 10, 2)
area = st.sidebar.number_input("Area (sqft)", min_value=200, max_value=10000, value=1200, step=50)
location_score = st.sidebar.selectbox("Location Score (1–10)", list(range(1, 11)))
age = st.sidebar.slider("Age of House (years)", 0, 100, 10)

# Prepare input
input_data = np.array([[bedrooms, bathrooms, area, location_score, age]])

# Predict
if st.button("🔮 Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated House Price: **${prediction[0]:,.2f}**")

# Footer
st.markdown("---", unsafe_allow_html=True)
st.markdown('<p class="footer">👩‍💻 Developed by <b>Siddiqa Ali</b></p>', unsafe_allow_html=True)
