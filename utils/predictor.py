import joblib
import pandas as pd

MODEL_FILE = "model.pkl"
PIPELINE_FILE = "pipeline.pkl"

def load_model():
    return joblib.load(MODEL_FILE)

def load_pipeline():
    return joblib.load(PIPELINE_FILE)

def dic(input_data):
    model = load_model()  # This is the full pipeline: preprocessor + classifier

    df = pd.DataFrame([input_data])

    # Pass raw data directly to the pipeline
    predictions = model.predict(df)
    
    return predictions[0]
