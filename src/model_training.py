import os
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from src.utils import read_csv, save_object, setup_logging

def train_linear_regression(data_path, model_output_path):
    """
    Train a Linear Regression model on the feature-engineered dataset.

    Args:
        data_path (str): Path to the feature-engineered dataset.
        model_output_path (str): Path where the trained model will be saved.
    """
    # Setup logging
    setup_logging()

    # Step 1: Load the dataset
    logging.info(f"Loading feature-engineered dataset from {data_path}")
    df = read_csv(data_path)

    # Separate features (X) and target (y)
    X = df.drop(columns=["tons_2012"])  # Target column is "tons_2012"
    y = df["tons_2012"]

    # Step 2: Split the data into training and testing sets
    logging.info("Splitting the dataset into training and testing sets.")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 3: Train a Linear Regression model
    logging.info("Training Linear Regression model.")
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)

    # Step 4: Evaluate the model
    logging.info("Evaluating the Linear Regression model on the test set.")
    y_pred = lr_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)  # Calculate MSE
    rmse = mse ** 0.5  # Calculate RMSE manually
    r2 = r2_score(y_test, y_pred)

    logging.info(f"Model Evaluation - MSE: {mse:.4f}, RMSE: {rmse:.4f}, R²: {r2:.4f}")
    print(f"Model Evaluation - MSE: {mse:.4f}, RMSE: {rmse:.4f}, R²: {r2:.4f}")

    # Step 5: Save the trained model
    logging.info(f"Saving the trained Linear Regression model to {model_output_path}")
    save_object(lr_model, model_output_path)


if __name__ == "__main__":
    # Define file paths
    feature_engineered_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/freight_analysis_feature_engineered.csv"
    model_output_path = "C:/project/Freight_Analysis_Framework-/models/lr_model.pkl"

    # Call the train_linear_regression function
    train_linear_regression(feature_engineered_data_path, model_output_path)

