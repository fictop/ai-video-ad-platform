from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    """Health check endpoint."""
    return "AI Video Ad Platform Backend (Placeholder) is Running!", 200

@app.route("/generate-video", methods=["POST", "OPTIONS"])
def generate_video():
    """Optional placeholder endpoint."""
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    data = request.get_json(silent=True) or {}
    product_name = data.get("product_name", "Unknown Product")
    return jsonify({"message": f"Generating video for {product_name}", "status": "success"})

@app.route("/create-ad", methods=["POST", "OPTIONS", "GET"])
def create_ad():
    """Main endpoint for ad generation (placeholder)."""
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    if request.method == "GET":
        return jsonify({"message": "Please use POST to create an ad", "status": "error"}), 405

    data = request.get_json(silent=True) or {}
    product_name = data.get("product_name", "Demo Product")

    # Placeholder logic
    return jsonify({
        "message": "Video ad generated successfully (placeholder)",
        "product": product_name,
        "status": "success"
    })

def _handle_cors_preflight():
    """Helper for CORS preflight."""
    resp = jsonify({})
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    resp.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return resp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
