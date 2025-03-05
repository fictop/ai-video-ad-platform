from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Allow all frontend requests

@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!"

@app.route("/generate-video", methods=["POST"])
def generate_video():
    data = request.json  
    product_name = data.get("product_name", "Unknown Product")
    return jsonify({"message": f"Generating video for {product_name}", "status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
