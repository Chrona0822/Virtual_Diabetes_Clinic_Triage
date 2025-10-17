import pytest
from src.api import app


valid_input = {
    "age": 0.02,
    "sex": -0.044,
    "bmi": 0.06,
    "bp": -0.03,
    "s1": -0.02,
    "s2": 0.03,
    "s3": -0.02,
    "s4": 0.02,
    "s5": 0.02,
    "s6": -0.001,
}

invalid_input = {"age": "invalid", "sex": -0.044, "bmi": 0.06}


@pytest.fixture(scope="module")
def client():
    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert "model_version" in data
    assert isinstance(data["model_version"], str)


def test_predict_valid_input(client):
    response = client.post("/predict", json=valid_input)
    assert response.status_code == 200
    data = response.get_json()
    assert "prediction" in data
    assert isinstance(data["prediction"], float)


def test_predict_invalid_input(client):
    response = client.post("/predict", json=invalid_input)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
