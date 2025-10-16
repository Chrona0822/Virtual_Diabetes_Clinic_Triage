from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
import joblib
import json

# load data
X, y = load_diabetes(return_X_y=True, as_frame=True)

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# v1 StandardScaler + LinearRegression
scaler = StandardScaler()
model = LinearRegression()

X_train_scaled = scaler.fit_transform(X_train)
model.fit(X_train_scaled, y_train)

# evaluate
X_test_scaled = scaler.transform(X_test)
y_pred = model.predict(X_test_scaled)
rmse = root_mean_squared_error(y_test, y_pred)

print(f"v0.1 RMSE: {rmse}")


# save model and scaler
pipeline = {"scaler": scaler, "model": model}
joblib.dump(pipeline, "diabetes_pipeline_v0.1.pkl")


# save metrics
metrics = {"rmse": rmse}
with open("metrics_v0.1.json", "w") as f:
    json.dump(metrics, f)
