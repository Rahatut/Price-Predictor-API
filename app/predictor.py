import numpy as np
import pandas as pd

def build_features(request, feature_cols):
    data = {
        "arrival": request.arrival,
        "minimum_price": request.minimum_price,
        "maximum_price": request.maximum_price,

        "day_of_week": request.day_of_week,
        "month": request.month,
        "day_of_year": request.day_of_year,

        "price_lag_1": request.price_lag_1,
        "price_lag_7": request.price_lag_7,
        "price_lag_30": request.price_lag_30,

        "rolling_mean_7": request.rolling_mean_7,
        "rolling_mean_30": request.rolling_mean_30,
        "rolling_std_7": request.rolling_std_7,

        "momentum_7": request.momentum_7,

        "price_pct_change_7": request.price_pct_change_7,
        "arrival_lag_1": request.arrival_lag_1,
        "arrival_rolling_7": request.arrival_rolling_7,
    }

    df = pd.DataFrame([data])

    return df[feature_cols]