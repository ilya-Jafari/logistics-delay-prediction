#for testing the model columns
import joblib

try:
    cols = joblib.load('model_columns.pkl')
    print("model expected columns: ")
    for c in cols:
        print(f"'{c}'")
except:
    print("file model_columns.pkl did not load")