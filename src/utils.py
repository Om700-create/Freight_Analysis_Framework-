import os
import logging
import pandas as pd
import pickle

def setup_logging(log_file_path="logs/project.log"):
    """
    Configures logging for the project.
    """
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Logging setup complete.")

def read_csv(file_path):
    """
    Reads a CSV file and returns a DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    logging.info(f"Loading data from {file_path}")
    return pd.read_csv(file_path)

def save_csv(data, file_path):
    """
    Saves a DataFrame to a CSV file.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    data.to_csv(file_path, index=False)
    logging.info(f"Data saved to {file_path}")

def save_object(obj, filename):
    """
    Save a Python object to a file using pickle.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)
    logging.info(f"Object saved to {filename}")

def load_object(filename):
    """
    Load a Python object from a file using pickle.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    with open(filename, 'rb') as f:
        obj = pickle.load(f)
    logging.info(f"Object loaded from {filename}")
    return obj
