from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# get version of model
MODEL_VERSION = "0.1" 
MODEL_PATH = f'diabetes_pipeline_v{MODEL_VERSION}.pkl'

# load model
try:
    pipeline = joblib.load(MODEL_PATH)
    print(f"Model {MODEL_PATH} loaded successfully.")
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_PATH}")
    pipeline = None

@app.route('/health', methods=['GET'])
def health():
    """check health endpoint"""
    return jsonify({"status": "ok", "model_version": MODEL_VERSION})

@app.route('/predict', methods=['POST'])
def predict():
    """predict endpoint"""
    if not pipeline:
        return jsonify({"error": "Model is not loaded."}), 500

    try:
        data = request.get_json()
        # transferm input data to DataFrame
        features = pd.DataFrame(data, index=[0])
        
        # make prediction
        scaler = pipeline['scaler']
        model = pipeline['model']
        
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)
        
        return jsonify({"prediction": prediction[0]})

    except Exception as e:
        # handle exceptions
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    # run app
    app.run(host='0.0.0.0', port=8000)
