import logging
import os
from src.utils import load_data, save_data, save_object, load_object

def setup_logging():
    """
    Ensures that the logs directory exists and configures logging.
    """
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "project.log")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Logging setup complete.")

if __name__ == "__main__":
    setup_logging()

    logging.info("Testing utility functions")

    # Test load_data and save_data
    data_path = "C:/project/Freight_Analysis_Framework-/data/raw/FAF4_Regional.csv"
    df = load_data(data_path)
    processed_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/test_data.csv"
    save_data(df, processed_data_path)

    # Test save_object and load_object
    test_object = {"key": "value", "number": 42}
    object_path = "C:/project/Freight_Analysis_Framework-/models/test_object.pkl"
    save_object(test_object, object_path)

    loaded_object = load_object(object_path)
    logging.info(f"Loaded object: {loaded_object}")

    logging.info("All utility function tests completed successfully.")

