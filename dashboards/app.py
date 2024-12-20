from flask import Flask, render_template, request
import pandas as pd
from src.utils import load_model

app = Flask(__name__)

# Load the trained model
model = load_model('models/lr_model.pkl')  # Ensure the path is correct

# Predefined feature columns based on the model
feature_columns = [
    'Log_Freight_Value_2012',
    'Log_Freight_Volume_2012',
    'Log_Volume_Value_Interaction_2012',
    'Value_Category_2012_Low',
    'Value_Growth_2012_2013',
    'Volume_Category_2012_Low',
    'Value_Growth_2013_2014',
    'Value_Growth_2014_2015',
    'Volume_Growth_2012_2013',
    'Volume_Growth_2013_2014'
]

# Load data for summary (from predictions CSV or another data source)
summary_data_path = 'models/predictions.csv'

@app.route('/')
def home():
    # Display summary statistics
    try:
        predictions = pd.read_csv(summary_data_path)
        summary = predictions.describe().to_html(classes="table table-striped", border=0)
    except Exception as e:
        summary = f"<p>Error loading summary data: {e}</p>"

    return render_template('index.html', summary=summary)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None

    if request.method == 'POST':
        try:
            # Retrieve the form data
            feature1 = float(request.form.get('feature1'))
            feature2 = float(request.form.get('feature2'))

            # Dynamically construct missing features
            input_data = pd.DataFrame([{
                'Log_Freight_Value_2012': feature1,
                'Log_Freight_Volume_2012': feature2,
                'Log_Volume_Value_Interaction_2012': feature1 * feature2,
                'Value_Category_2012_Low': 1 if feature1 < 0.5 else 0,
                'Value_Growth_2012_2013': feature2 * 1.02,
                'Volume_Category_2012_Low': 1 if feature2 < 0.3 else 0,
                'Value_Growth_2013_2014': feature1 * 0.98,
                'Value_Growth_2014_2015': feature1 * 1.03,
                'Volume_Growth_2012_2013': feature2 * 1.01,
                'Volume_Growth_2013_2014': feature2 * 0.99
            }])

            # Reorder columns to match the training feature order
            input_data = input_data[feature_columns]

            # Make predictions
            prediction = model.predict(input_data)[0]

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)





