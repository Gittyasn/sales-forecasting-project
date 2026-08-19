import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from typing import Tuple, Dict, Any

def train_sales_model(df: pd.DataFrame) -> Tuple[LinearRegression, Dict[str, float]]:
    """Trains a Linear Regression model on sales features.
    
    Returns the trained model and dictionary of evaluation metrics (MAE, RMSE).
    """
    # Features: Month, Day, Hour, Weekday, Quantity Ordered, Price Each
    X = df[['Month', 'Day', 'Hour', 'Weekday', 'Quantity Ordered', 'Price Each']]
    y = df['Sales']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Model training
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluation
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    metrics = {
        'MAE': mae,
        'RMSE': rmse
    }
    
    return model, metrics

def predict_sales(model: LinearRegression, features: pd.DataFrame) -> np.ndarray:
    """Predicts Sales based on input features using the trained model."""
    # Features must contain: Month, Day, Hour, Weekday, Quantity Ordered, Price Each
    return model.predict(features)

def forecast_next_month(model: LinearRegression, df: pd.DataFrame) -> float:
    """Forecasts the average sales per order for the next month based on historical mean.
    
    Uses historical data from the last month in the dataset as baseline.
    """
    last_month = df['Month'].max()
    next_month = 1 if last_month == 12 else last_month + 1
    
    next_month_data = df[df['Month'] == last_month].copy()
    next_month_data['Month'] = next_month
    
    features = next_month_data[['Month', 'Day', 'Hour', 'Weekday', 'Quantity Ordered', 'Price Each']]
    predictions = predict_sales(model, features)
    return float(predictions.mean())
