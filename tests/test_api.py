from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_predict_returns_price():
	payload = {
		"arrival": 1.2,
		"minimum_price": 2000,
		"maximum_price": 2500,
		"day_of_week": 2,
		"month": 5,
		"day_of_year": 150,
		"price_lag_1": 2400,
		"price_lag_7": 2350,
		"price_lag_30": 2200,
		"rolling_mean_7": 2380,
		"rolling_mean_30": 2300,
		"rolling_std_7": 40,
		"momentum_7": 50,
		"price_pct_change_7": 0.02,
		"arrival_lag_1": 1.1,
		"arrival_rolling_7": 1.3,
	}

	response = client.post("/predict", json=payload)

	assert response.status_code == 200
	body = response.json()
	assert "predicted_price" in body
	assert isinstance(body["predicted_price"], (int, float))
