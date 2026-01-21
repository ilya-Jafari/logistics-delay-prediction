import streamlit as st
import pandas as pd
import joblib

# Page configuration for a professional look
st.set_page_config(page_title="Logistics Intelligence", page_icon="🚚", layout="wide")

# 1. Load the saved model and columns
model = joblib.load('logistic_delay_model.pkl')
model_columns = joblib.load('model_columns.pkl')

# --- UI Header ---
st.title("🚚 Smart Logistics: AI Delay Predictor")
st.markdown("""
This application uses a **Random Forest Machine Learning model** to analyze shipment data 
and predict the probability of delivery delays.
""")
st.divider()

# --- Layout: Columns ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.subheader("📋 Shipment Parameters")
    st.info("Input the details of the upcoming shipment below.")
    
    # Input fields in the sidebar/column
    shipment_type = st.selectbox("Payment Type", ["DEBIT", "TRANSFER", "CASH", "PAYMENT"])
    region = st.selectbox("Order Region", ["Western Europe", "Central America", "South America", "Southeast Asia"])
    shipping_mode = st.selectbox("Shipping Mode", ["Standard Class", "First Class", "Second Class", "Same Day"])
    segment = st.selectbox("Customer Segment", ["Consumer", "Corporate", "Home Office"])
    
    predict_btn = st.button("Analyze Risk", use_container_width=True, type="primary")

with col2:
    st.subheader("📊 Prediction Results")
    
    if predict_btn:
        # Process Input
        input_df = pd.DataFrame(0, index=[0], columns=model_columns)
        if f'Type_{shipment_type}' in model_columns: input_df[f'Type_{shipment_type}'] = 1
        if f'Order Region_{region}' in model_columns: input_df[f'Order Region_{region}'] = 1
        if f'Shipping Mode_{shipping_mode}' in model_columns: input_df[f'Shipping Mode_{shipping_mode}'] = 1
        if f'Customer Segment_{segment}' in model_columns: input_df[f'Customer Segment_{segment}'] = 1
        
        # Make Prediction
        probability = model.predict_proba(input_df)[0][1]
        
        # Display as a Metric and Alert
        risk_level = "HIGH RISK" if probability > 0.5 else "LOW RISK"
        color = "red" if probability > 0.5 else "green"
        
        st.metric(label="Delay Probability", value=f"{probability:.2%}", delta=risk_level, delta_color="inverse" if probability > 0.5 else "normal")
        
        if probability > 0.5:
            st.error(f"**Warning:** This shipment has a high risk of being delayed. Consider changing the shipping mode.")
        else:
            st.success(f"**Safe:** This shipment is likely to arrive on time according to the AI model.")
            
        # Optional: Add a small bar chart for visual probability
        st.bar_chart({"Risk Level": [probability, 1-probability]}, horizontal=True)
    else:
        st.write("Enter data on the left and click 'Analyze Risk' to see the result.")

# --- Footer ---
st.divider()
st.caption("Built with Python & Streamlit | Powered by Random Forest Classifier")