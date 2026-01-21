import streamlit as st
import pandas as pd
import joblib

# 1. Load the saved model and columns
model = joblib.load('logistic_delay_model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title("🚚 Logistics Delay Predictor")
st.write("Enter shipment details to calculate the probability of delay.")

# 2. Create Input Fields for the User
st.sidebar.header("Shipment Details")

shipment_type = st.sidebar.selectbox("Payment Type", ["DEBIT", "TRANSFER", "CASH", "PAYMENT"])
region = st.sidebar.selectbox("Order Region", ["Western Europe", "Central America", "South America", "Southeast Asia"])
shipping_mode = st.sidebar.selectbox("Shipping Mode", ["Standard Class", "First Class", "Second Class", "Same Day"])
segment = st.sidebar.selectbox("Customer Segment", ["Consumer", "Corporate", "Home Office"])

# 3. Process Input for Prediction
if st.button("Predict Delay Probability"):
    # Create a template dataframe with all zeros
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    
    # Fill the template based on user input (One-Hot Encoding match)
    if f'Type_{shipment_type}' in model_columns: input_df[f'Type_{shipment_type}'] = 1
    if f'Order Region_{region}' in model_columns: input_df[f'Order Region_{region}'] = 1
    if f'Shipping Mode_{shipping_mode}' in model_columns: input_df[f'Shipping Mode_{shipping_mode}'] = 1
    if f'Customer Segment_{segment}' in model_columns: input_df[f'Customer Segment_{segment}'] = 1
    
    # 4. Make Prediction
    probability = model.predict_proba(input_df)[0][1]
    
    # 5. Show Results
    st.subheader(f"Prediction Result")
    if probability > 0.5:
        st.error(f"High Risk: {probability:.2%}")
    else:
        st.success(f"Low Risk: {probability:.2%}")