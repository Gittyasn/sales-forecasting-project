# 📊 Sales Forecasting & Business Intelligence Platform

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Streamlit](https://img.shields.io/badge/Powered%20By-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📝 Project Overview
This platform transforms raw retail sales data into actionable business intelligence. It features a robust, modular backend for data processing and a high-performance interactive dashboard for exploratory analysis and predictive forecasting.

### 🎯 Objective
To provide stakeholders with a comprehensive tool for monitoring sales performance, identifying peak seasonal trends, and projecting future revenue using machine learning.

---

## ✨ Key Features
- **Professional Architecture**: Fully modular Python codebase following SOLID principles.
- **Automated Data Pipeline**: Intelligent cleaning, date standardization, and feature extraction.
- **Interactive Analytics**: Dynamic Plotly visualizations for temporal and product-based trends.
- **ML Forecast Engine**: Integrated Linear Regression model with automated performance evaluation (MAE/RMSE).
- **Production-Ready Dashboard**: Polished Streamlit UI with custom styling and logging.

---

## 🛠️ Tech Stack
| Category | Technologies |
| :--- | :--- |
| **Language** | Python 3.8+ |
| **Data Engine** | Pandas, NumPy |
| **Visuals** | Plotly, Matplotlib, Seaborn |
| **Machine Learning**| Scikit-Learn |
| **UI/UX** | Streamlit, Custom CSS |

---

## 📂 Repository Structure
```text
sales-product-data/
├── data/                       # Dataset directory
│   └── Sales_Product_Combined.csv
├── src/                        # Modular source files
│   ├── loader.py               # Data ingestion & caching
│   ├── preprocessing.py        # Feature engineering & cleaning
│   └── model.py                # Machine learning training & prediction
├── app.py                      # Interactive Streamlit dashboard
├── Sales_Product.py            # Standalone CLI analysis script
├── requirements.txt            # Package dependencies
└── README.md                   # System documentation
```

---

## 🚀 Setup & Execution Guide

### 1. Environment Setup
Create a virtual environment and install the required dependencies:
```powershell
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows Command Prompt:
.\venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Interactive Dashboard
Launch the interactive Streamlit dashboard:
```powershell
# Run the Streamlit app
streamlit run app.py

# Alternatively, call Streamlit directly from the venv folder:
.\venv\Scripts\streamlit run app.py
```

### 3. Running the Standalone CLI Analysis
To run the analysis directly in your terminal:
```powershell
python Sales_Product.py
```

---

## 📉 Core Business Insights
*   **Temporal Seasonality**: Sales exhibit a ~30% surge during Q4 holiday cycles.
*   **Peak Demand Windows**: Maximum customer engagement occurs at **12:00 PM** and **7:00 PM** daily.
*   **Revenue Drivers**: iPhone and Macbook Pro constitute the primary revenue share.

---
*Developed for Portfolio Excellence*
