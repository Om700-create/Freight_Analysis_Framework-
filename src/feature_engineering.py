import pandas as pd
import logging
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utils import read_csv, save_csv, setup_logging

def handle_invalid_values(df):
    """
    Handles invalid values (NaN, Inf, -Inf) in the dataset.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Replace infinite values with NaN
    df = df.replace([np.inf, -np.inf], np.nan)

    # Fill NaN values with column median for numerical columns
    for col in df.select_dtypes(include=[np.number]).columns:
        if df[col].isnull().any():
            median_value = df[col].median()
            df[col] = df[col].fillna(median_value)

    return df

def feature_engineer(input_path, output_path):
    """
    Perform feature engineering on the processed dataset.

    Args:
        input_path (str): Path to the processed data file.
        output_path (str): Path where the feature-engineered data will be saved.
    """
    # Setup logging
    setup_logging()

    # Step 1: Load the processed data
    df = read_csv(input_path)
    logging.info(f"Loaded processed dataset with shape: {df.shape}")

    # Step 2: Handle invalid values
    logging.info("Handling invalid values (NaN, Inf, -Inf)...")
    df = handle_invalid_values(df)

    # Step 3: Define transformations
    categorical_columns = df.select_dtypes(include=['object']).columns
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

    # Numerical scaling
    num_scaler = StandardScaler()

    # One-hot encoding for categorical variables
    cat_encoder = OneHotEncoder(handle_unknown='ignore')

    # Combine transformations
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_scaler, numerical_columns),
            ('cat', cat_encoder, categorical_columns)
        ]
    )

    # Step 4: Apply transformations
    logging.info("Applying transformations...")
    transformed_data = preprocessor.fit_transform(df)

    # Combine transformed data with column names
    num_features = numerical_columns
    cat_features = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_columns)
    feature_names = list(num_features) + list(cat_features)

    transformed_df = pd.DataFrame(transformed_data, columns=feature_names)

    logging.info(f"Feature engineering completed. New dataset shape: {transformed_df.shape}")

    # Step 5: Save the feature-engineered dataset
    save_csv(transformed_df, output_path)
    logging.info(f"Feature-engineered dataset saved to {output_path}")

if __name__ == "__main__":
    # Define file paths
    processed_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/freight_analysis_cleaned.csv"
    feature_engineered_data_path = "C:/project/Freight_Analysis_Framework-/data/processed/freight_analysis_feature_engineered.csv"

    # Call the feature engineering function
    feature_engineer(processed_data_path, feature_engineered_data_path)



