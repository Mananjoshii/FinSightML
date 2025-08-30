# Loan Default Prediction System

This project is a web application for predicting loan defaults using a trained machine learning model. The application allows users to input loan-related data and receive predictions on whether a loan will be approved or not.

## Project Structure

```
loan-default-web-app
├── src
│   ├── app.py                # Main entry point of the web application
│   ├── templates
│   │   └── index.html        # HTML template for the web interface
│   ├── static
│   │   └── style.css         # CSS styles for the web interface
│   └── utils
│       └── predictor.py      # Functions for loading the model and making predictions
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── loan.csv                  # Dataset used for training the model
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd loan-default-web-app
   ```

2. **Install dependencies**:
   Create a virtual environment and activate it, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the following command to start the Flask web server:
   ```
   python src/app.py
   ```

4. **Access the web interface**:
   Open your web browser and navigate to `http://127.0.0.1:5000` to access the loan default prediction interface.

## Usage Guidelines

- Input the required loan data in the provided fields on the web interface.
- Click the "Predict" button to receive a prediction on loan approval.
- The application will display the prediction result on the same page.

## Additional Information

- The `loan.csv` file contains the dataset used for training the model and is referenced in the `predictor.py` for making predictions.
- Ensure that the model is trained and saved before running the web application.

## License

This project is licensed under the MIT License.