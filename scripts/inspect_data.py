import pandas as pd
import os

file_path = "data/DataCoSupplyChainDataset.csv"

try:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    print("✅ File loaded successfully!")
    
    print("\n--- 1. ALL COLUMNS ---")
    print(df.columns.tolist())
    
    print("\n--- 2. SAMPLE DATA (First 3 rows) ---")
    pd.set_option('display.max_columns', None)
    print(df.head(3))
    
    print("\n--- 3. POTENTIAL CANDIDATES ---")
    date_cols = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
    print(f"Date Columns found: {date_cols}")
    
    status_cols = [col for col in df.columns if 'status' in col.lower()]
    print(f"Status Columns found: {status_cols}")

except FileNotFoundError:
    print(f"❌ Error: File not found at {file_path}. Make sure the CSV is in the 'data' folder.")
except Exception as e:
    print(f"❌ Error: {e}")