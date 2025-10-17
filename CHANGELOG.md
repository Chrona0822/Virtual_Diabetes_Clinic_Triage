```markdown
# Changelog

## v0.2
- **Features**:
  - Baseline model using `StandardScaler` and `RandomForestRegressor`.

- **Metrics**:
  - RMSE: 54.3984
  - Evaluating 'high-risk' flag using threshold > 150.0
  - Precision: 0.6957
  - Recall: 0.8000

## v0.1 - Initial Release

- **Features**:
  - Baseline model using `StandardScaler` and `LinearRegression`.
  - Flask API with `/health` and `/predict` endpoints.
  - Dockerized application for portability.
  - CI/CD pipelines using GitHub Actions for testing and releasing.
- **Metrics**:
  - RMSE on test set: [53.85344583676594]