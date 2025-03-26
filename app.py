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
@app.route("/create-ad", methods=["POST"])
def create_ad():
    # Use a test video URL known to work reliably.
    sample_video_url = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/Big_Buck_Bunny_360_10s_1MB.mp4"
    return jsonify({
        "message": "Video ad generated successfully (test video)",
        "video_url": sample_video_url,
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
