import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# ✅ Allow only your frontend domain to prevent CORS issues
CORS(app, origins=["https://fictop.com"], supports_credentials=True)

@app.route("/")
def home():
    return "✅ AI Video Ad Platform Backend is Running!", 200

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "✅ Test endpoint is working!"}), 200

@app.route("/create-ad", methods=["POST", "GET"])
def create_ad():
    sample_video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
    return jsonify({
        "message": "✅ Video ad generated successfully (test video)",
        "video_url": sample_video_url,
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use default port 10000 or environment PORT
    app.run(host="0.0.0.0", port=port)
