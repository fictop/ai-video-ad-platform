from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def health_check():
    return "AI Video Ad Platform Backend is Running!", 200

@app.route("/generate-video", methods=["POST", "OPTIONS"])
def generate_video():
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    data = request.json or {}
    product_name = data.get("product_name", "Unknown Product")
    return jsonify({"message": f"Generating video for {product_name}", "status": "success"})

@app.route("/create-ad", methods=["POST", "OPTIONS", "GET"])
def create_ad():
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    if request.method == "GET":
        return jsonify({"message": "Please use POST to create an ad", "status": "error"}), 405

    data = request.json or {}
    product_name = data.get("product_name", "Demo Product")
    prompt = data.get("prompt", "A professional avatar for advertisement")

    # Just a placeholder flow:
    avatar_image = "avatar.png"
    final_video = "final_ad.mp4"
    return jsonify({
        "message": "Video ad generated successfully (test mode)",
        "product_name": product_name,
        "prompt": prompt,
        "avatar": avatar_image,
        "video_url": final_video,
        "status": "success"
    })

def _handle_cors_preflight():
    resp = jsonify({})
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    resp.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return resp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
