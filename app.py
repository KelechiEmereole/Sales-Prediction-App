import numpy as np
import pandas as pd
import joblib
import streamlit as st
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import StandardScaler

# Load the model,
try:
        loaded_model = joblib.load('gbr_model.sav')
except FileNotFoundError as e:
    st.error(f"Model file not found: {e}")
    loaded_model = None

# Load LabelEncoders
try:
        label_encoders = joblib.load('label_encoders.pkl')
except FileNotFoundError:
    st.error("LabelEncoders file not found.  Make sure 'label_encoders.pkl' is in the correct location.")
    label_encoders = None

# Load Scaler
try:
    scaler = joblib.load("scaler.pkl")
except FileNotFoundError:
    st.error("Scaler file not found. Make sure 'scaler.pkl' is in the correct location.")
    scaler = None

def main():
    
    st.title('Supermarket Sales Prediction App')
    
    # Choose mode
    mode = st.radio("Choose Prediction Mode:", ["Formula (Exact)", "Machine Learning (Approximate)"])

    col1, col2= st.columns(2)

    with col1:
       gender = st.selectbox("Gender", ["Male", "Female"])
       branch = st.selectbox("Branch", ["A", "B", "C"])
       city = st.selectbox("City", ["Yangon", "Mandalay", "Naypyitaw"])  
       customer_type = st.selectbox("Customer Type", ["Member", "Normal"])

    with col2:
       product_line = st.selectbox("Product Line", 
                                ["Health and beauty", "Electronic accessories", 
                                 "Home and lifestyle", "Sports and travel", 
                                 "Food and beverages", "Fashion accessories"])
       unit_price = st.number_input("Unit Price", min_value=0.0, step=0.1)
       quantity = st.number_input("Quantity", min_value=1, max_value=10, step=1)
       tax_5 = st.number_input("Tax (5%)", min_value=0.0, step=0.1, format="%.3f")
         
    if st.button("Predict / Calculate", use_container_width=True):
        if mode == "Formula (Exact)":
            # Direct formula: unit_price * quantity + tax_5
            total_sales = (unit_price * quantity) + tax_5
            st.success(f"✅ Exact Total Sales: ${total_sales:,.3f}")

        elif mode == "Machine Learning (Approximate)":
            if loaded_model is not None and scaler is not None:  
                input_data = pd.DataFrame({
                    'gender': [gender],
                    'branch': [branch],
                    'city': [city],
                    'customer_type': [customer_type],
                    'product_line': [product_line],
                    'unit_price': [unit_price],
                    'quantity': [quantity],
                    'tax_5%': [tax_5]
                })

        
        # Encode categorical columns before prediction
                for col in ['gender', 'branch', 'city', 'customer_type', 'product_line']:
                    input_data[col] = label_encoders[col].transform(input_data[col])

                try:
                     input_scaled = scaler.transform(input_data)

                     prediction = loaded_model.predict(input_scaled)  

                     predicted_sales = prediction[0]  
     
                     st.success(f" Predicted Total Sales: ${predicted_sales:,.3f}")
    
                except Exception as e:
                     st.error(f"Prediction failed: {e}")
            else:
                st.error("❌ Model or LabelEncoders not loaded. Please check the files.")

if __name__ == '__main__':
    main()