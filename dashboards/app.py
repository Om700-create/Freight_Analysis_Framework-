from flask import Flask, render_template, request
import pandas as pd
from src.utils import load_model

app = Flask(__name__)

# Load the trained model
model = load_model('models/lr_model.pkl')  # Ensure the path is correct

# Predefined feature columns based on your model
feature_columns = [
    'Log_Freight_Value_2012',
    'Log_Freight_Volume_2012',
    'Log_Volume_Value_Interaction_2012',
    'Value_Category_2012_Low',
    'Value_Growth_2012_2013'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None

    if request.method == 'POST':
        # Retrieve the form data
        feature1 = float(request.form.get('feature1'))
        feature2 = float(request.form.get('feature2'))

        # Construct the input DataFrame
        input_data = pd.DataFrame([{
            'Log_Freight_Value_2012': feature1,
            'Log_Freight_Volume_2012': feature2,
            'Log_Volume_Value_Interaction_2012': feature1 * feature2,
            'Value_Category_2012_Low': 1 if feature1 < 0.5 else 0,
            'Value_Growth_2012_2013': feature2 * 1.02  # Example logic
        }])

        # Make predictions
        try:
            prediction = model.predict(input_data)[0]  # Get the first value of prediction
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)




