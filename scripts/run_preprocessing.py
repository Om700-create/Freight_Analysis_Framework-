import logging
from src.utils import setup_logging
from src.data_preprocessing import preprocess_data

if __name__ == "__main__":
    # Setup logging
    setup_logging()

    logging.info("Starting the preprocessing script.")

    # File paths
    raw_data_path = "C:/project/Freight_Analysis_Framework-/data/raw/FAF4_Regional.csv"
    processed_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/freight_analysis_cleaned.csv"

    try:
        # Run preprocessing
        preprocess_data(raw_data_path, processed_data_path)
        logging.info("Preprocessing completed successfully.")
    except Exception as e:
        logging.error(f"Error during preprocessing: {e}")
