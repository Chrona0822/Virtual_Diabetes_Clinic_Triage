from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import root_mean_squared_error, precision_score, recall_score
import joblib
import json

# load data
X, y = load_diabetes(return_X_y=True, as_frame=True)

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# # v1 StandardScaler + LinearRegression
# scaler = StandardScaler()
# model = LinearRegression()

# X_train_scaled = scaler.fit_transform(X_train)
# model.fit(X_train_scaled, y_train)

# # evaluate
# X_test_scaled = scaler.transform(X_test)
# y_pred = model.predict(X_test_scaled)
# rmse = root_mean_squared_error(y_test, y_pred)

# print(f"v0.1 RMSE: {rmse}")


# # save model and scaler
# pipeline = {"scaler": scaler, "model": model}
# joblib.dump(pipeline, "diabetes_pipeline_v0.1.pkl")


# # save metrics
# metrics = {"rmse": rmse}
# with open("metrics_v0.1.json", "w") as f:
#     json.dump(metrics, f)


# --- 2. Define and Train the v0.2 Model Pipeline ---

print("\nTraining Model v0.2 (StandardScaler + RandomForestRegressor)...")
pipeline_v2 = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("model", RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)),
    ]
)

# Train the entire pipeline on the training data.
pipeline_v2.fit(X_train, y_train)
print("Model training complete.")

# --- 3. Evaluate the Model ---
print("\nEvaluating model performance on the test set...")
y_pred = pipeline_v2.predict(X_test)

# a) Calculate Root Mean Squared Error (RMSE)
rmse = root_mean_squared_error(y_test, y_pred)
print(f"  - RMSE: {rmse:.4f}")

# b) Evaluate the "high-risk" flag
# Define a threshold for what constitutes a "high-risk" patient.
HIGH_RISK_THRESHOLD = 150.0
print(f"  - Evaluating 'high-risk' flag using threshold > {HIGH_RISK_THRESHOLD}")

# Convert actual and predicted values to boolean flags.
y_test_flag = y_test > HIGH_RISK_THRESHOLD
y_pred_flag = y_pred > HIGH_RISK_THRESHOLD

# Calculate precision and recall for the classification task.
precision = precision_score(y_test_flag, y_pred_flag)
recall = recall_score(y_test_flag, y_pred_flag)

print(f"  - Precision: {precision:.4f}")
print(f"  - Recall: {recall:.4f}")

# --- 4. Save the Pipeline and Metrics ---
# Save the trained pipeline object to a file.
model_filename = "diabetes_pipeline_v0.2.pkl"
joblib.dump(pipeline_v2, model_filename)
print(f"\nModel pipeline saved successfully to '{model_filename}'")

# Save the calculated metrics to a JSON file for tracking.
metrics = {
    "model_version": "0.2",
    "rmse": rmse,
    "high_risk_threshold": HIGH_RISK_THRESHOLD,
    "precision": precision,
    "recall": recall,
}
metrics_filename = "metrics_v0.2.json"
with open(metrics_filename, "w") as f:
    json.dump(metrics, f, indent=4)
print(f"Performance metrics saved successfully to '{metrics_filename}'")
