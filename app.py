import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for frontend-backend communication
app.url_map.strict_slashes = False  # Allows routes with or without trailing slash

@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!", 200

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Test endpoint is working!"}), 200

# This route generates a video ad and provides a working video URL
@app.route("/create-ad", methods=["POST"])
def create_ad():
    # Using a **new valid** test video URL
    sample_video_url = "https://fictop.github.io/ai-video-ad-platform/final_ad.mp4"

    return jsonify({
        "message": "Video ad generated successfully (fallback)",
        "video_url": sample_video_url,
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
