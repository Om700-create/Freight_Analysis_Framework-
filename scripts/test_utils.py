import logging
from src.utils import read_csv, save_csv, save_object, load_object, setup_logging

def test_utils():
    """
    Test the utility functions in the src/utils.py module.
    """
    setup_logging()
    logging.info("Testing utility functions...")

    # Test read_csv and save_csv
    try:
        data_path = "data/raw/FAF4_Regional.csv"
        processed_path = "data/processed/test_data.csv"

        df = read_csv(data_path)
        logging.info(f"Data loaded successfully with shape: {df.shape}")

        save_csv(df, processed_path)
        logging.info(f"Data saved successfully to {processed_path}")
    except Exception as e:
        logging.error(f"Error in read_csv/save_csv: {e}")

    # Test save_object and load_object
    try:
        test_object = {"key": "value", "number": 42}
        object_path = "models/test_object.pkl"

        save_object(test_object, object_path)
        loaded_object = load_object(object_path)
        logging.info(f"Object loaded successfully: {loaded_object}")
    except Exception as e:
        logging.error(f"Error in save_object/load_object: {e}")

    logging.info("All utility tests completed successfully.")

if __name__ == "__main__":
    test_utils()
