import pandas as pd
import streamlit as st

@st.cache_data
def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans and preprocesses the raw Sales Product dataframe.
    
    Includes date conversions, type conversions, removing invalid rows,
    and feature engineering for analysis and modeling.
    """
    # Create a copy to prevent SettingWithCopy warnings
    df = df.copy()
    
    # Clean column names (strip whitespace)
    df.columns = df.columns.str.strip()
    
    # Rename 'Price' to 'Price Each' if necessary
    if 'Price' in df.columns and 'Price Each' not in df.columns:
        df.rename(columns={'Price': 'Price Each'}, inplace=True)
        
    # Combine Order Date and Time if Time exists
    if 'Time' in df.columns:
        # Ensure both are strings before concatenating
        df['Order Date'] = df['Order Date'].astype(str) + ' ' + df['Time'].astype(str)
        
    # Convert 'Order Date' to datetime with dayfirst=True for '19-04-2019' format
    # Using errors='coerce' to handle header rows or invalid formats
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    
    # Convert Quantity Ordered and Price Each to numeric
    # errors='coerce' turns non-numeric (like header rows) to NaN
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
    df['Price Each'] = pd.to_numeric(df['Price Each'], errors='coerce')
    
    # Drop rows with NaN values (headers, missing data, invalid parsing)
    df = df.dropna()
    
    # Extract time-related features
    df['Month'] = df['Order Date'].dt.month
    df['Day'] = df['Order Date'].dt.day
    df['Hour'] = df['Order Date'].dt.hour
    df['Weekday'] = df['Order Date'].dt.weekday  # Monday=0, Sunday=6
    
    # Create Sales column
    df['Sales'] = df['Quantity Ordered'] * df['Price Each']
    
    return df
