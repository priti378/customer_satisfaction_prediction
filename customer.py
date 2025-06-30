import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model
with open("satisfaction_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load trained column names
with open("feature_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

st.title("Customer Satisfaction Prediction")

# Raw input
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.slider("Age", 18, 70)
product = st.selectbox("Product Purchased", [
    "Amazon Echo", "Amazon Fire TV", "Amazon Kindle", "Amazon Video", "Fire Tablet"
])
issue_type = st.selectbox("Issue Type", ["Billing", "Technical", "Account", "Other"])
ticket_channel = st.selectbox("Ticket Channel", ["Email", "Chat", "Phone"])

# Build DataFrame with raw values
input_dict = {
    "Customer Age": age,
    "Customer Gender": gender,
    "Product Purchased": product,
    "Issue Type": issue_type,
    "Ticket Channel": ticket_channel
}

input_df = pd.DataFrame([input_dict])

# Apply same preprocessing as during training
input_encoded = pd.get_dummies(input_df)

# Reindex to match training columns (fill missing with 0)
input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

# Predict
if st.button("Predict Satisfaction"):
    prediction = model.predict(input_encoded)[0]
    label = "Satisfied" if prediction == 1 else "Not Satisfied"
    st.success(f"Predicted: {label}")
