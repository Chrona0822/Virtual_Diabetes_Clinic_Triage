import pytest
import requests

base_url = "http://localhost:8000"

valid_input = {    "age": 0.02, "sex": -0.044, "bmi": 0.06, "bp": -0.03,
    "s1": -0.02, "s2": 0.03, "s3": -0.02, "s4": 0.02,
    "s5": 0.02, "s6": -0.001 }

invalid_input = {"age": "invalid", "sex": -0.044, "bmi": 0.06}

def test_health_check():
    response = requests.get(f"{base_url}/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "model_version" in data

def test_predict_valid_input():
    response = requests.post(f"{base_url}/predict", json=valid_input)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], float)

def test_predict_invalid_input():
    response = requests.post(f"{base_url}/predict", json=invalid_input)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data