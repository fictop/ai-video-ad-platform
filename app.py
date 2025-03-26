import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False  # Allow routes with or without trailing slash

@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!", 200

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Test endpoint is working!"}), 200

# For testing, we bypass dynamic generation and return a known-good sample video URL.
@app.route("/create-ad", methods=["POST", "GET"])
def create_ad():
    # Use a reliable test video URL from W3Schools.
    sample_video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
    return jsonify({
        "message": "Video ad generated successfully (test video)",
        "video_url": sample_video_url,
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
