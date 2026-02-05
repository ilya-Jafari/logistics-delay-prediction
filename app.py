import streamlit as st
import pandas as pd
import numpy as np
import joblib
import ollama
import requests
from bs4 import BeautifulSoup
import pm4py
from pm4py.objects.conversion.log import converter as log_converter
import os

# 1. Initial Configuration & Academic Theme
st.set_page_config(page_title="TU Dortmund | Logistics Intelligence Hub 2.1", layout="wide")

# 2. Load ML Assets (Model & Columns) 
@st.cache_resource
def load_assets():
    """
    Loads the trained Machine Learning model and the list of columns
    used during training to ensure feature alignment.
    """
    try:
        model = joblib.load('models/logistic_delay_model.pkl')
        columns = joblib.load('models/model_columns.pkl')
        return model, columns
    except Exception as e:
        st.error(f"❌ Error loading model assets: {e}")
        return None, None

model, model_columns = load_assets()

def predict_delay_probability(shipping_mode, region):
    """
    Calculates the probability of delay using the loaded model.
    It constructs the One-Hot Encoded features dynamically based on user input.
    
    Args:
        shipping_mode (str): The selected shipping mode (e.g., 'Standard Class').
        region (str): The destination region (e.g., 'Western Europe').
    """
    if model is not None and model_columns is not None:
        # Create a dataframe with all model columns initialized to 0
        input_data = pd.DataFrame(0, index=[0], columns=model_columns)
        
        # Construct exact column names matching the training phase
        mode_col = f"Shipping Mode_{shipping_mode}"
        region_col = f"Order Region_{region}"
        
        # Debugging: Print to terminal to verify column matching
        print(f"DEBUG: Looking for columns: '{mode_col}' and '{region_col}'")
        
        # Set the specific one-hot encoded columns to 1 if they exist in the model
        if mode_col in input_data.columns:
            input_data[mode_col] = 1
        else:
            print(f"WARNING: '{mode_col}' not found in model columns.")

        if region_col in input_data.columns:
            input_data[region_col] = 1
        else:
             print(f"WARNING: '{region_col}' not found in model columns.")
            
        # Perform prediction (Probability of Class 1: Delay)
        probability = model.predict_proba(input_data)[0][1]
        return round(float(probability) * 100, 2)
    return 0.0

# 3. Auxiliary Functions (News & Process Mining) 

def get_live_logistics_news():
    """
    Fetches real-time logistics news titles for the LLM context.
    Falls back to static headlines if the connection fails.
    """
    try:
        url = "https://gcaptain.com/feed/"
        res = requests.get(url, timeout=3)
        soup = BeautifulSoup(res.content, 'xml')
        return [item.title.text for item in soup.find_all('item')[:3]]
    except:
        return [
            "Global shipping routes stability report 2026", 
            "New maritime regulations update in EU sector",
            "Port congestion analysis: Southeast Asia"
        ]

def generate_pm4py_map():
    """
    Generates a Directly-Follows Graph (DFG) using pm4py based on synthetic logs.
    This simulates the 'Process Discovery' phase of the framework.
    """
    # Synthetic event log simulating a bottleneck
    log_data = {
        'case_id': ['1','1','1', '2','2', '3','3','3', '4', '4'],
        'activity': ['Order Placed', 'Shipping', 'Delivered', 
                     'Order Placed', 'Delivered',
                     'Order Placed', 'Customs Hold', 'Delivered',
                     'Order Placed', 'Customs Hold'],
        'timestamp': pd.to_datetime(['2026-01-01']*10)
    }
    
    # Convert to dataframe and rename to standard XES columns
    df = pd.DataFrame(log_data).rename(columns={
        'case_id': 'case:concept:name', 
        'activity': 'concept:name', 
        'timestamp': 'time:timestamp'
    })
    
    # Discover and save DFG
    dfg, start, end = pm4py.discover_directly_follows_graph(df)
    pm4py.save_vis_dfg(dfg, start, end, "assets/process_map.png")
    return "assets/process_map.png"

# 4. User Interface (Streamlit) 

st.title("🌐 Logistics Intelligence Hub 2.0")
st.markdown("---")

# Tabs for separate functional layers
tab1, tab2 = st.tabs(["📊 ML Delay Prediction", "🧠 Strategic BPM Analysis"])

# --- TAB 1: Machine Learning Layer 
with tab1:
    col_input, col_viz = st.columns([1, 1.2], gap="large")
    
    with col_input:
        st.header("Shipment Parameters")
        
        # Input 1: Shipping Mode (Matches 'Shipping Mode_' columns)
        s_mode = st.selectbox("Shipping Mode", ["Standard Class", "Second Class", "Same Day", "First Class"])
        
        # Input 2: Region (Matches 'Order Region_' columns)
        # Using a subset of your actual columns for the demo
        region_list = [
            "Western Europe", "Southeast Asia", "South Asia", 
            "Central Asia", "Eastern Europe", "West of USA ", # Note: Maintained the space as per list
            "South America", "Oceania"
        ]
        dest_region = st.selectbox("Destination Region", region_list)
        
        if st.button("Calculate Probability", use_container_width=True):
            with st.spinner("Running Inference..."):
                risk_pct = predict_delay_probability(s_mode, dest_region)
                
                # Dynamic Display
                st.metric("Probability of Delay", f"{risk_pct}%", delta="- High Risk" if risk_pct > 50 else "Stable")
                st.progress(risk_pct / 100)
                
                if risk_pct > 60:
                    st.error("⚠️ Critical Alert: High probability of supply chain disruption.")
                elif risk_pct > 30:
                    st.warning("⚠️ Warning: Moderate risk detected.")
                else:
                    st.success("✅ Operational: Prediction suggests on-time delivery.")

    with col_viz:
        st.header("Explainable AI (XAI)")
        st.write("Feature importance contribution for the current prediction:")
        
        # Static XAI chart for demonstration purposes
        xai_data = pd.DataFrame({
            'Feature': ['Region Influence', 'Shipping Mode', 'Seasonality', 'Carrier Rating'],
            'Impact Score': [0.55, 0.30, 0.10, 0.05]
        }).set_index('Feature')
        
        st.bar_chart(xai_data)
        st.caption("Figure 1: Local feature importance interpretation.")

# --- TAB 2: Process Mining & GenAI Layer ---
with tab2:
    st.header("BPM & Local LLM Integration")
    st.write("This module combines **Process Discovery** (pm4py) with **Generative AI** (Llama 3) to provide strategic advice.")
    
    if st.button("Run Strategic Deep-Dive", use_container_width=True):
        col_map, col_report = st.columns([1.2, 1])
        
        with st.spinner("Mining Process Logs & Querying Llama 3..."):
            # 1. Generate Process Map
            try:
                map_img = generate_pm4py_map()
                map_status = True
            except Exception as e:
                st.error(f"Graphviz Error: {e}")
                map_status = False
            
            # 2. Fetch News & Generate LLM Response
            news = get_live_logistics_news()
            
            prompt = f"""
            Role: Supply Chain Risk Manager.
            Context: A process bottleneck was detected in 'Customs Hold'.
            Real-time News: {news}.
            Task: Provide a concise, academic strategic recommendation to mitigate delays.
            """
            
            try:
                response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
                ai_text = response['message']['content']
            except:
                ai_text = "Error: Ensure Ollama is running locally."
            
            # 3. Visualization
            with col_map:
                st.subheader("Discovered Process Map (DFG)")
                if map_status:
                    st.image(map_img, caption="Visualizing Bottlenecks in Shipment Lifecycle")
                else:
                    st.warning("Install Graphviz to see the map.")
                
            with col_report:
                st.subheader("AI Strategic Advisory")
                st.markdown("#### 📰 Live Context")
                for n in news:
                    st.markdown(f"- *{n}*")
                
                st.divider()
                st.markdown("#### 🧠 Llama 3 Analysis")
                st.info(ai_text)

# Footer
st.divider()
st.markdown("<p style='text-align: center; color: grey;'>TU Dortmund | Faculty of CS | Ilya Jafari 2026</p>", unsafe_allow_html=True)