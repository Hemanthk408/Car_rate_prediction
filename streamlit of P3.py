import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
model_path = "/mnt/data/Cars_price_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Define the Streamlit app
st.title("Car Price Prediction App 🚗💰")

st.write("Enter the car details below to predict the price!")

# Define input fields (modify as needed based on model requirements)
year = st.number_input("Year of Manufacture", min_value=2000, max_value=2025, value=2015, step=1)
mileage = st.number_input("Mileage (km)", min_value=0, max_value=500000, value=50000, step=5000)
engine_size = st.number_input("Engine Size (L)", min_value=0.5, max_value=6.0, value=1.6, step=0.1)

# Example categorical features (modify as needed)
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric", "Hybrid"])

# Convert categorical data to numerical (modify encoding as per model training)
transmission_encoded = 1 if transmission == "Automatic" else 0
fuel_mapping = {"Petrol": 0, "Diesel": 1, "Electric": 2, "Hybrid": 3}
fuel_encoded = fuel_mapping[fuel_type]

# Prepare input for prediction
features = np.array([[year, mileage, engine_size, transmission_encoded, fuel_encoded]])

# Predict price
if st.button("Predict Price"):
    price_prediction = model.predict(features)[0]
    st.success(f"Predicted Car Price: ${price_prediction:,.2f}")
