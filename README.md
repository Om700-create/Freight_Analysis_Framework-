# Freight Analysis Framework - Predictive Analytics

**Author:** Narayan Bhandari  
**Email:** narayanbhnadari498@gmail.com  

## Overview

This project is an end-to-end machine learning solution designed to analyze and predict freight trends using the Freight Analysis Framework dataset. The project includes data preprocessing, feature engineering, model training, and deployment through a Flask-based dashboard.

---

## Problem Statement

Freight management involves complex challenges, including:

- Managing fluctuations in freight volumes and values.
- Predicting future freight trends for optimized supply chain planning.
- Analyzing large datasets to derive actionable insights.

### Objective

The goal is to build a robust system that:
1. Processes and cleans freight data.
2. Engineers meaningful features to improve prediction accuracy.
3. Trains and evaluates machine learning models.
4. Deploys a dashboard for predictions and visualizations.

---

## Dataset Details

**Dataset Name:** FAF4 Regional Freight Analysis Dataset  
**Source:** Self-organized dataset  

### Key Features

- **Volume Metrics:** Freight volumes across years (2012-2045).
- **Value Metrics:** Freight values across years (2012-2045).
- **Geographic Data:** Origin and destination regions.
- **Categorical Variables:** Transportation modes, trade types.

### Data Summary

- Total Records: ~1.6M rows
- Final Features After Engineering: 64 columns
- Missing Data: Handled using imputation strategies.

---

## Methodology

1. **Data Preprocessing:**
   - Missing values handled using median/mode imputation.
   - Outlier detection and capping applied to freight volumes and values.

2. **Feature Engineering:**
   - Log transformations for scaling volume and value.
   - Interaction terms between key features.
   - One-hot encoding for categorical variables.

3. **Model Training:**
   - Evaluated Models:
     - Linear Regression
     - Gradient Boosting Regressor
     - Random Forest Regressor
   - Selected Model: Linear Regression (R²: 0.9995).

4. **Deployment:**
   - Flask dashboard for data visualization and predictions.
   - Input freight features to predict future trends.

---

## Key Observations

1. **Data Distribution:**
   - Freight volume and value showed a right-skewed distribution.
   - Seasonal fluctuations observed in certain regions.

2. **Model Performance:**
   - Achieved RMSE of 0.0217 and R² of 0.9995.
   - High correlation between freight volume and value metrics.

3. **Predictive Insights:**
   - Volume and value interactions significantly impacted predictions.
   - Seasonal trends highlight the importance of strategic planning.

---

## Project Structure

```plaintext
project/
│
├── data/
│   ├── raw/                # Original dataset
│   ├── processed/          # Processed and feature-engineered datasets
│   ├── interim/            # Temporary intermediate files
│
├── notebooks/              # Jupyter notebooks for exploratory analysis
│   ├── 01_eda.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_modeling.ipynb
│   ├── 05_visualization.ipynb
│
├── src/                    # Source code
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── visualization.py
│   ├── utils.py
│
├── dashboards/             # Flask dashboard
│   ├── app.py              # Flask app
│   ├── templates/          # HTML templates for the dashboard
│       ├── index.html
│       ├── predict.html
│
├── scripts/                # Pipeline scripts
│   ├── run_preprocessing.py
│   ├── run_training.py
│   ├── run_dashboard.py
│
├── models/                 # Saved models and predictions
│
├── logs/                   # Log files
│
├── reports/                # Reports
│   ├── final_report.pdf
│
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies

Running the Project
Set up the environment:

Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run Data Preprocessing:

bash
Copy code
python scripts/run_preprocessing.py
Run Feature Engineering:

bash
Copy code
python scripts/test_feature_engineering.py
Train the Model:

bash
Copy code
python scripts/run_training.py
Launch the Dashboard:

bash
Copy code
python scripts/run_dashboard.py
Access the Dashboard: Open http://127.0.0.1:5000 in your web browser.

Contact
Author: Narayan Bhandari
Email: narayanbhnadari498@gmail.com
Project: Freight Analysis Framework - Predictive Analytics

Note: This project is a demonstration of machine learning applications for freight analysis and should be further tuned for specific business use cases.

Copy code






