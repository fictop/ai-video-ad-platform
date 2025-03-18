<<<<<<< HEAD
from flask import Flask 
app = Flask(__name__) 
@app.route("/") 
def home(): return "Hello, Flask!" 
if __name__ == "__main__": app.run(debug=True) 
=======
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

# For testing, we bypass dynamic generation and return our static sample video URL.
@app.route("/create-ad", methods=["POST"])
def create_ad():
    # Replace the URL below with the full URL where your sample video is hosted.
    sample_video_url = "https://fictop.github.io/ai-video-ad-platform/final_ad.mp4"
    return jsonify({
        "message": "Video ad generated successfully (fallback)",
        "video_url": sample_video_url,
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
>>>>>>> 639c89a08ae7c5e068e40e0d1c476429ff62791b
