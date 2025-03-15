import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False  # Allow routes with or without trailing slash

@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!", 200

# Simple test endpoint to verify routing
@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Test endpoint is working!"}), 200

# For now, we use the static sample video as a fallback.
@app.route("/create-ad", methods=["POST"])
def create_ad():
    # Instead of dynamic generation, return the sample video.
    return jsonify({
        "message": "Video ad generated successfully (fallback)",
        "video_url": "final_ad.mp4",
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
