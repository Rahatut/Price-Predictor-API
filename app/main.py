from fastapi import FastAPI
from app.model_loader import load_model
from app.schemas import PredictionRequest
from app.predictor import build_features

import numpy as np

model, feature_cols = load_model()

app = FastAPI(title="Price Prediction API")


@app.get("/")
def home():
    return {"status": "API running"}


@app.post("/predict")
def predict(req: PredictionRequest):

    X = build_features(req, feature_cols)

    pred = model.predict(X)[0]

    return {
        "predicted_price": float(pred)
    }