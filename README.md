# 🏡 House Price Prediction App

A simple, pastel-themed Streamlit web app to predict house prices based on user inputs.

---

## Features

- Interactive sidebar inputs:
  - Bedrooms
  - Bathrooms
  - Area (sqft)
  - Location score (1–10)
  - Age of the house
- Real-time house price prediction using a pre-trained machine learning model.
- Custom pastel theme with CSS styling.
- Easy-to-use, beginner-friendly interface.

---

## Demo Screenshot

*(Add your app screenshot here if available)*

---

## Installation

1. Clone the repository:

    python
    git clone <your-repo-url>
    cd <repo-folder>

2. Create a virtual environment (optional but recommended):

    python
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

3. Install dependencies:

    python
    pip install -r requirements.txt

4. Make sure you have the model file in the correct path:

    assets/model.pkl

---

## Usage

Run the app:

    python
    streamlit run app.py

- Use the sidebar to enter house details.
- Click **🔮 Predict Price** to see the estimated house price.

---

## Dependencies

- Python 3.x  
- Streamlit  
- scikit-learn / joblib  
- numpy  

*(You can generate `requirements.txt` by running `pip freeze > requirements.txt`)*

---

## Developer

👩‍💻 Developed by **Siddiqa Ali**

---

## License

MIT License
