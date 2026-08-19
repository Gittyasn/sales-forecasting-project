import os
import pandas as pd
import streamlit as st

@st.cache_data
def load_dataset(file_path: str = 'data/Sales_Product_Combined.csv') -> pd.DataFrame:
    """Loads the Sales Product dataset from CSV.
    
    Uses Streamlit's cache_data for fast re-runs.
    """
    if not os.path.exists(file_path):
        # Support running from within the src/ directory or root directory
        alternate_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), file_path)
        if os.path.exists(alternate_path):
            file_path = alternate_path
        else:
            raise FileNotFoundError(f"Dataset file '{file_path}' not found.")
            
    df = pd.read_csv(file_path)
    return df
