# Commodity Price Forecasting System

A machine learning-based forecasting system for predicting commodity market prices using historical time-series data and engineered market indicators.

The project trains an XGBoost regression model on commodity market data and exposes predictions through a FastAPI backend for real-time inference.

---

Commodity prices fluctuate due to changing market conditions, supply variations, seasonality, and demand trends. Accurate forecasting can help improve market planning, pricing analysis, and supply-chain decision making.

This project aims to build a production-oriented forecasting pipeline that:

* processes historical commodity market data
* engineers temporal forecasting features
* trains a machine learning regression model
* serves predictions through a REST API

---

## System Architecture

```text id="archclean"
                ┌────────────────────┐
                │ Historical Dataset │
                └─────────┬──────────┘
                          ↓
              ┌──────────────────────┐
              │ Feature Engineering  │
              │ - Lag Features       │
              │ - Rolling Statistics │
              │ - Momentum Signals   │
              │ - Seasonal Features  │
              └─────────┬────────────┘
                        ↓
               ┌─────────────────┐
               │ XGBoost Model   │
               │ Time-Series ML  │
               └────────┬────────┘
                        ↓
            ┌─────────────────────┐
            │ FastAPI Inference   │
            │ REST Prediction API │
            └──────────┬──────────┘
                       ↓
                Predicted Price
```

---

## Features

### Machine Learning Forecasting

* XGBoost regression model for commodity price prediction
* Time-series-aware train/test splitting
* Forecasting based on historical market behavior

### Feature Engineering

* Lag-based temporal features
* Rolling averages and volatility indicators
* Momentum and trend signals
* Calendar-based seasonal features

### FastAPI Backend Service

* Real-time prediction API
* Interactive Swagger documentation
* Structured inference pipeline
* JSON-based request/response handling

### Model Evaluation

* MAE
* RMSE
* R² Score
* MAPE

---

## Tech Stack

### ML & Data

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Development

* Jupyter Notebook
* Git
* Virtual Environment (venv)

---

