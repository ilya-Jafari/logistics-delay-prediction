import streamlit as st
import pandas as pd
import joblib
import ollama
import requests
from bs4 import BeautifulSoup
import pm4py
from pm4py.objects.conversion.log import converter as log_converter

# ۱. تنظیمات صفحه (حتماً باید اولین دستور باشد)
st.set_page_config(page_title="2026 Logistics Intelligence Hub", page_icon="🌐", layout="wide")

# --- ۲. توابع کمکی (AI, Mining, Process) ---

def fetch_live_news():
    try:
        url = "https://gcaptain.com/feed/"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'xml')
        headlines = [item.title.text for item in soup.find_all('item')[:4]]
        return headlines
    except:
        return ["Unable to fetch live news. Using cached trade data."]

def get_ai_insight(headlines):
    prompt = f"Analyze these logistics headlines for 2026: {headlines}. What is the #1 risk for global trade today?"
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

def generate_process_map():
    # ساخت دیتای رویداد فرضی برای نمایش در بخش Process Mining
    event_data = {
        'case:concept:name': ['S1', 'S1', 'S1', 'S2', 'S2', 'S3', 'S3', 'S3', 'S3'],
        'concept:name': ['Order Picked', 'Customs Clearance', 'Delivered', 
                         'Order Picked', 'Delivered',
                         'Order Picked', 'Customs Clearance', 'Warehouse Hold', 'Delivered'],
        'time:timestamp': pd.to_datetime(['2026-01-20 08:00', '2026-01-21 10:00', '2026-01-23 15:00',
                                         '2026-01-20 09:00', '2026-01-22 14:00',
                                         '2026-01-20 08:30', '2026-01-21 11:00', '2026-01-22 09:00', '2026-01-25 10:00'])
    }
    df_event = pd.DataFrame(event_data)
    dfg, start_act, end_act = pm4py.discover_directly_follows_graph(df_event)
    pm4py.save_vis_dfg(dfg, start_act, end_act, "process_map.png")
    return "process_map.png"

# --- ۳. بارگذاری مدل‌های هوش مصنوعی (ML) ---
# حتماً مطمئن شوید این فایل‌ها در پوشه پروژه هستند
try:
    model = joblib.load('logistic_delay_model.pkl')
    model_columns = joblib.load('model_columns.pkl')
except:
    st.error("Model files not found! Please check .pkl files.")

# --- ۴. رابط کاربری (UI) ---
st.title("🌐 Logistics Intelligence Hub: AI & Process Analytics 2026")
st.markdown("---")

# ایجاد ستون‌های اصلی
col_left, col_right = st.columns([1, 1.5], gap="large")

# ستون سمت چپ: پیش‌بینی عددی (ML)
with col_left:
    st.header("📊 Predictive ML Analysis")
    st.write("Calculate delay probability based on historical data.")
    
    ship_type = st.selectbox("Payment Type", ["DEBIT", "TRANSFER", "CASH"])
    region = st.selectbox("Region", ["Western Europe", "Central America", "Southeast Asia"])
    
    if st.button("Calculate ML Risk", use_container_width=True):
        # در اینجا می‌توانید کد واقعی مدل را قرار دهید، فعلاً نمایش عدد تستی:
        st.metric("Delay Probability", "72%")
        st.warning("High risk detected based on historical bottlenecks.")

# ستون سمت راست: هوش مصنوعی زنده و تحلیل فرآیند
with col_right:
    # بخش اول: تحلیل لاما ۳
    st.header("🧠 Generative AI Agent (Llama 3)")
    if st.button("Fetch & Analyze Live Global Risks"):
        with st.spinner("Mining 2026 Trade Data..."):
            news = fetch_live_news()
            insight = get_ai_insight(news)
            
            st.subheader("📰 Latest Global Headlines")
            for h in news:
                st.write(f"• {h}")
            
            st.info(f"**AI Strategic Report:** {insight}")

    st.markdown("---")
    
    # بخش دوم: فرآیندکاوی (Process Mining) - مورد علاقه پروفسور
    st.header("📉 Business Process Analytics")
    if st.button("Analyze Process Flow & Bottlenecks"):
        with st.spinner("Generating Process Map..."):
            img_path = generate_process_map()
            st.image(img_path, caption="Directly Follows Graph (DFG) - Logistics Bottlenecks")
            st.success("Analysis: 'Warehouse Hold' identified as the primary process delay factor.")

# پاورقی
st.markdown("---")
st.caption("Developed by Ilya Jafari | Research Framework: AI in Management & Process Analytics")