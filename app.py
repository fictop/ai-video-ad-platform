from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# VERY IMPORTANT: allow only your frontend domain here
CORS(app, resources={r"/*": {"origins": "https://fictop.com"}}, supports_credentials=True)

@app.route("/")
def home():
    return "✅ AI Video Ad Platform Backend is Running!", 200

@app.route("/test")
def test():
    return jsonify({"message": "✅ Test endpoint is working!"})

@app.route("/create-ad", methods=["POST", "GET"])
def create_ad():
    return jsonify({
        "message": "✅ Video ad generated successfully (test video)",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "status": "success"
    })
