from pydantic import BaseModel

class PredictionRequest(BaseModel):
    arrival: float
    minimum_price: float
    maximum_price: float

    day_of_week: int
    month: int
    day_of_year: int

    price_lag_1: float
    price_lag_7: float
    price_lag_30: float

    rolling_mean_7: float
    rolling_mean_30: float
    rolling_std_7: float

    momentum_7: float

    price_pct_change_7: float
    arrival_lag_1: float
    arrival_rolling_7: float