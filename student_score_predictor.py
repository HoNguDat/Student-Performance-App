from flask import Flask, request, jsonify, send_from_directory
import joblib
import pandas as pd
from flask_cors import CORS
import os

model = joblib.load("student_performance_model.pkl")

app = Flask(__name__)
# Mở khóa toàn bộ cấu hình CORS ở mức tối đa
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return send_from_directory(os.getcwd(), "index.html")

@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():
    if request.method == "OPTIONS":
        response = jsonify({"status": "OK"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response, 200
        
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])
        prediction = model.predict(input_df)
        
        response = jsonify({"predicted_score": float(prediction[0])})
        response.headers.add("Access-Control-Allow-Origin", "*") 
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)