# scripts/run_training.py

import logging
from src.model_training import train_linear_regression
from src.utils import setup_logging

if __name__ == "__main__":
    # Setup logging
    setup_logging()

    logging.info("Starting the model training pipeline.")

    # Define file paths
    feature_engineered_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/freight_analysis_feature_engineered.csv"
    model_output_path = "C:/project/Freight_Analysis_Framework-/models/lr_model.pkl"

    try:
        # Train the Linear Regression model
        train_linear_regression(feature_engineered_data_path, model_output_path)

        logging.info("Model training pipeline completed successfully.")
    except Exception as e:
        logging.error(f"Error during model training: {e}")
        print(f"Error: {e}")