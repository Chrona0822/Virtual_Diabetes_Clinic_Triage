```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [v0.2] - 2025-10-17

### Changed
- **Model Improvement**: Replaced the baseline `LinearRegression` model with a `RandomForestRegressor` wrapped in a `scikit-learn` Pipeline for better performance and easier preprocessing.
- **API Version**: Updated the `/health` endpoint to report model version "0.2".
- **Evaluation Metrics**: Added Precision and Recall for a "high-risk" flag (progression > 150) to better evaluate model performance for clinical triage.

### Metrics Comparison

| Metric    | v0.1 (Linear Regression) | v0.2 (Random Forest) |  
| :-------- | :----------------------- | :------------------- |  
| **RMSE**  | `53.85344583676594`      | `54.3984`            | 
| Precision | N/A                      | `0.6957`             |
| Recall    | N/A                      | `0.8000`             | 

---

## [v0.1] - [2025-10-16]
Initial Release

### Added
- Initial release of the Diabetes Progression Prediction Service.
- **Baseline Model**: Implemented with `StandardScaler` and `LinearRegression`.
- **API**: Created a Flask API with `/health` and `/predict` endpoints.
- **Containerization**: Packaged the application as a self-contained Docker image.
- **CI/CD**: Set up GitHub Actions for automated testing (`ci.yml`) and releases (`release.yml`).

### Metrics
- **RMSE**: `[53.85344583676594]`