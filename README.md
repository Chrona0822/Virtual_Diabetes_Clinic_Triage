# Virtual_Diabetes_Clinic_Triage
Hi, this ML service predicts short-term disease progression and returns a continuous risk score.

* **v0.1**: Baseline model using `StandardScaler` and `LinearRegression`.
* **v0.2**: Improved model using a `Pipeline` with `StandardScaler` and `RandomForestRegressor`. This version also provides precision/recall metrics for a "high-risk" flag.

See `CHANGELOG.md` for detailed performance metrics

## How to Run Locally

### Prerequisites
- Docker installed and running.

### Steps
1.  **Build the Docker Image:**
    Replace `<version>` with the version you want to run (e.g., `v0.1` or `v0.2`).
    ```bash
    docker build -t diabetes-service:<version> .
    ```

2.  **Run the Docker Container:**
   Make sure to use the same `<version>` tag from the build step.
    ```bash
    docker run -d -p 8000:8000 --name diabetes-container diabetes-service:<version>
    ```
    The service will now be running in the background and accessible at `http://localhost:8000`.

3.  **Stop and Remove the Container when finished:**
    ```bash
    docker stop diabetes-container && docker rm diabetes-container
    ```

## API Endpoints

### Health Check

- **URL:** `/health`
```bash
curl http://localhost:8000/health
```
- **Method:** `GET`
- **Success Response (200 OK):**
  ```json
  {
    "model_version": "0.1",
    "status": "ok"
  }

### Predcition

- **URL:** `/predict`
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"age": 0.02, "sex": -0.044, "bmi": 0.06, "bp": -0.03, "s1": -0.02, "s2": 0.03, "s3": -0.02, "s4": 0.02, "s5": 0.02, "s6": -0.001}' \
  http://localhost:8000/predict
```
- **Method:** `POST`
- **Request Body(JSON):**
- A JSON object with the 10 features
```json
{
  "age": 0.02, "sex": -0.044, "bmi": 0.06, "bp": -0.03,
  "s1": -0.02, "s2": 0.03, "s3": -0.02, "s4": 0.02,
  "s5": 0.02, "s6": -0.001
}
```
- **Success Response (200 OK):**
{
  "prediction": 235.94963722176266
}

- **Error Response (400 Bad Request):**
{
  "error": "Details about the error."
}


