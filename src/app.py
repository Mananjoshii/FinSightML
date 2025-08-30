from flask import Flask, render_template, request
import pandas as pd
import joblib
from utils.predictor import dic

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.form.to_dict()
    prediction = dic(input_data)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
