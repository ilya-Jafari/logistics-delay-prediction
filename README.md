# 🌐 Logistics Intelligence Hub 2.1 (2026 Edition)
### Predictive ML + Real-Time Data Mining + Local LLM Analysis
![Project Demo](assets/demo.gif)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red)
![Ollama](https://img.shields.io/badge/AI-Llama3-orange)
![License](https://img.shields.io/badge/License-MIT-green)
> **Towards Trustworthy and Generative Process Analytics:** A hybrid framework for real-time logistics risk management using Local LLMs.

---

## 🧐 The Problem: Why this Project?

In the modern logistics landscape (2026 Context), traditional predictive systems face a critical limitation: **They are "Black Boxes" that only output numbers, not strategies.**

* **Standard ML:** Tells you *with 72% probability* that a shipment will be delayed.
* **The Missing Link:** It doesn't tell you *why* structurally (Process Bottleneck) or *what to do* about it (Strategy).

Supply chain managers are drowning in data but starving for insights. They need a system that bridges the gap between **Quantitative Risk** (numbers) and **Qualitative Context** (real-world events).

## 💡 The Solution: Tri-Layer Intelligence

This project introduces a **Multi-Agent Intelligence Hub** that operates on three distinct layers to ensure robust and actionable decision support:

### 1. 📊 The Predictive Layer (Machine Learning)
* **Technology:** Scikit-Learn (Logistic Regression with Robust Scaling).
* **Function:** Analyzes structured shipment data (Region, Shipping Mode, Carrier).
* **Output:** A precise **Delay Probability Score** with One-Hot Encoded feature mapping.
* **XAI:** Explains *which* features contributed most to the risk.

### 2. 🔍 The Descriptive Layer (Process Mining)
* **Technology:** `pm4py` (Python Process Mining).
* **Function:** Mines event logs to discover the underlying **Directly-Follows Graph (DFG)**.
* **Output:** Visual identification of structural bottlenecks (e.g., *'Customs Hold'* loops) that purely numerical models miss.

### 3. 🧠 The Prescriptive Layer (Generative AI)
* **Technology:** **Local Llama 3** (via Ollama).
* **Function:** Acts as a "Strategic Consultant." It fuses the ML risk score + Process Map + Real-time Logistics News.
* **Output:** Human-readable, strategic advice (e.g., *"Due to high risk in Southeast Asia and customs bottlenecks, reroute via Rotterdam..."*).

--- 

## 📌 Project Overview
The **Logistics Intelligence Hub** is a next-generation decision-support system designed to mitigate supply chain risks. Unlike traditional dashboards that rely on static historical data, this platform combines **Machine Learning** with **Live Data Mining** and **Generative AI** to provide actionable insights for global logistics managers in 2026.

## 🚀 Key Features
- **Predictive Analytics:** Uses a trained Random Forest model to calculate the probability of shipment delays based on historical shipping patterns, payment types, and regional factors.
- **Real-Time Data Mining:** Automatically scrapes and parses live logistics news from global RSS feeds (e.g., gCaptain, Loadstar) to capture the pulse of the industry.
- **Local AI Intelligence:** Integrated with **Llama 3 via Ollama** to analyze unstructured news data. It identifies geopolitical risks, port strikes, and maritime threats without sending sensitive data to the cloud.
- **Interactive UI:** A high-performance Streamlit dashboard that bridges the gap between raw data and executive decision-making.

## 🛠 Tech Stack
- **Core:** Python 3.10+
- **Machine Learning:** Scikit-Learn, Pandas, NumPy
- **Generative AI:** Ollama, Llama 3 (Local LLM)
- **Data Scraping:** BeautifulSoup4, lxml, Requests
- **Visualization:** Streamlit, Tableau

---
![Logistics Dashboard](assets/dashboard.png)

## 🗺 The Vision: Roadmap to 3.0 (Scale & Future Growth)
This project is architected for massive scalability. While version 2.0 is a powerful diagnostic tool, it serves as the foundation for a **Fully Autonomous Logistics Ecosystem**:

### 1. Multi-Agent Workflows (Autonomous Agents)
Implementing frameworks like **CrewAI** or **LangGraph** to create a team of AI agents:
* *The Scout:* 24/7 autonomous web monitoring for specific port disruptions.
* *The Strategist:* Cross-references news with internal ML predictions to suggest alternative shipping routes.

### 2. Long-Term Memory (Vector Databases)
Integrating **ChromaDB** or **Pinecone** to store historical disruptions. This allows the AI to learn from the past (e.g., *"This strike in Rotterdam resembles the 2024 crisis, suggesting a 15-day recovery window"*).

### 3. Real-Time IoT & Asset Tracking
Expanding data input from static forms to live **API integrations** with GPS and AIS (Automatic Identification System) to track vessels and trucks in real-time on a global map.

---

## 🛠️ Repository Structure

The project follows a modular research-grade structure:

```text
Logistics_AI_Project/
│
├── app.py                  # Main application entry point (Streamlit)
├── requirements.txt        # Project dependencies
│
├── models/                 # Pre-trained ML models (Frozen Assets)
│   ├── logistic_delay_model.pkl
│   └── model_columns.pkl
│
├── assets/                 # Generated visualizations & static images
│   ├── dashboard.png
│   └── process_map.png
│
├── data/                   # Synthetic training logs & datasets
│   └── DataCoSupplyChainDataset.csv
│
└── README.md               # Documentation