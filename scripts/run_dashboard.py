# Python script
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from src.visualization import plot_actual_vs_predicted, plot_residuals
from src.utils import read_csv

# Define file paths
processed_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/freight_analysis_feature_engineered.csv"
predictions_path = "C:/project/Freight_Analysis_Framework-/models/predictions.csv"

# Load data
data = read_csv(processed_data_path)
predictions = read_csv(predictions_path)

# Extract actual and predicted values
y_test = predictions['Actual']
y_pred = predictions['Predicted']

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Freight Analysis Dashboard", style={"textAlign": "center"}),

    dcc.Tabs([
        dcc.Tab(label="Actual vs Predicted", children=[
            html.Div([
                dcc.Graph(figure=plot_actual_vs_predicted(y_test, y_pred))
            ])
        ]),
        dcc.Tab(label="Residuals", children=[
            html.Div([
                dcc.Graph(figure=plot_residuals(y_test, y_pred))
            ])
        ])
    ])
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
