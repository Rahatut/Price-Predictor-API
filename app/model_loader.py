import pickle
import json
from pathlib import Path

MODEL_DIR = Path(__file__).resolve().parents[1] / "model"

def load_model():
    with open(MODEL_DIR / "model.pkl", "rb") as f:
        model = pickle.load(f)

    with open(MODEL_DIR / "feature_cols.json", "r") as f:
        features = json.load(f)

    return model, features