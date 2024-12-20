# src/visualization.py

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

def plot_actual_vs_predicted(y_test, y_pred):
    """
    Create a scatter plot comparing actual vs. predicted values.

    Args:
        y_test (pd.Series): Actual target values.
        y_pred (pd.Series): Predicted target values.

    Returns:
        fig: Plotly figure object.
    """
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    fig = px.scatter(df, x="Actual", y="Predicted", title="Actual vs Predicted",
                     labels={"Actual": "Actual Values", "Predicted": "Predicted Values"},
                     template="plotly_white")
    fig.add_shape(type='line', x0=0, y0=0, x1=df['Actual'].max(), y1=df['Actual'].max(),
                  line=dict(color="Red", dash="dash"))
    return fig

def plot_residuals(y_test, y_pred):
    """
    Create a residual plot.

    Args:
        y_test (pd.Series): Actual target values.
        y_pred (pd.Series): Predicted target values.

    Returns:
        fig: Plotly figure object.
    """
    residuals = y_test - y_pred
    fig = px.scatter(x=y_test, y=residuals, title="Residual Plot",
                     labels={"x": "Actual Values", "y": "Residuals"},
                     template="plotly_white")
    fig.add_hline(y=0, line_dash="dash", line_color="red")
    return fig

def save_visualization(fig, file_path):
    """
    Save the visualization to a file.

    Args:
        fig (go.Figure): Plotly figure object.
        file_path (str): File path to save the visualization.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    fig.write_html(file_path)
    print(f"Visualization saved to {file_path}")
