# models/train_model.py

import pandas as pd
import joblib
import lightgbm as lgb
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
import sys
import os
import xgboost as xgb
# Ensure the project root is in the PYTHONPATH for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.preprocess import load_data, clean_data, get_features_target

def main():
    # Load the dataset (update the path to your CSV file)
    filepath = 'C:/Users/syedn/Desktop (1)/projects/House price prediction/data/Indian_House_Prices.csv'
    df = load_data(filepath)
    
    # Clean the data
    df_clean = clean_data(df)
    
    # Define the selected features (adjust as needed)
    feature_cols = [
        'Area', 
        'No. of Bedrooms', 
        'Resale', 
        'SwimmingPool', 
        'CarParking', 
        'School', 
        'LiftAvailable', 
        'MaintenanceStaff', 
        'Location', 
        'City'
    ]
    
    # Split into features and target
    X, y = get_features_target(df_clean, feature_cols, target_col='Price')
    
    # Split the data into training and test sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  

# Initialize and train the XGBoost Regressor
    xgb_model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
    xgb_model.fit(X_train, y_train)

# Predict on the test set
    y_pred_xgb = xgb_model.predict(X_test)

# Evaluate performance
    print("XGBoost Performance:")
    print("R² Score:", r2_score(y_test, y_pred_xgb))
    print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred_xgb))
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred_xgb))
    print("Root Mean Squared Error:", np.sqrt(mean_squared_error(y_test, y_pred_xgb)))
    
  
    
    # Save the trained model
    model_path = 'models/xgb_model.pkl'
    joblib.dump(xgb_model, model_path)
    print("Model saved to:", model_path)
    
if __name__ == "__main__":
    main()
