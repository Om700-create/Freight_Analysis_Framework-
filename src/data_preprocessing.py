import pandas as pd
from sklearn.impute import SimpleImputer
from src.utils import read_csv, save_csv, setup_logging

def preprocess_data(input_path, output_path):
    """
    Perform data preprocessing on the raw dataset.

    Args:
        input_path (str): Path to the raw data file.
        output_path (str): Path where the processed data will be saved.
    """
    # Setup logging
    setup_logging()

    # Step 1: Load the raw data
    df = read_csv(input_path)
    logging.info(f"Loaded dataset with shape: {df.shape}")

    # Step 2: Handle missing values
    # Separate columns by data type
    categorical_columns = df.select_dtypes(include=['object']).columns
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

    # Impute categorical columns with the mode
    cat_imputer = SimpleImputer(strategy="most_frequent")
    df[categorical_columns] = cat_imputer.fit_transform(df[categorical_columns])

    # Impute numerical columns with the median
    num_imputer = SimpleImputer(strategy="median")
    df[numerical_columns] = num_imputer.fit_transform(df[numerical_columns])

    logging.info("Handled missing values in the dataset.")

    # Step 3: Save the processed dataset
    save_csv(df, output_path)
    logging.info(f"Processed dataset saved to: {output_path}")


if __name__ == "__main__":
    raw_data_path = "C:/project/Freight_Analysis_Framework-/data/raw/FAF4_Regional.csv"
    processed_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/freight_analysis_cleaned.csv"
    preprocess_data(raw_data_path, processed_data_path)
