import logging
from src.feature_engineering import feature_engineer
from src.utils import setup_logging

if __name__ == "__main__":
    # Setup logging
    setup_logging()

    logging.info("Testing feature engineering pipeline.")

    # Define file paths
    processed_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/freight_analysis_cleaned.csv"
    feature_engineered_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/freight_analysis_feature_engineered.csv"

    try:
        # Run feature engineering
        feature_engineer(processed_data_path, feature_engineered_data_path)
        logging.info("Feature engineering pipeline completed successfully.")
    except Exception as e:
        logging.error(f"Error during feature engineering: {e}")
        print(f"Error: {e}")
