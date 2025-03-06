from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Define the Flask app and enable CORS for all routes
app = Flask(__name__)
CORS(app)

# Home endpoint
@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!"

# Existing /generate-video endpoint (optional)
@app.route("/generate-video", methods=["POST", "OPTIONS"])
def generate_video():
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    
    data = request.json or {}
    product_name = data.get("product_name", "Unknown Product")
    
    return jsonify({"message": f"Generating video for {product_name}", "status": "success"})

# New integrated endpoint for creating an ad with the full AI pipeline
@app.route("/create-ad", methods=["POST", "OPTIONS"])
def create_ad():
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    
    data = request.json or {}
    product_name = data.get("product_name", "Demo Product")
    prompt = data.get("prompt", "A professional avatar for advertisement")
    
    try:
        # Placeholder processing steps:
        avatar_image = generate_avatar(prompt)       # returns "avatar.png"
        animated_video = animate_avatar(avatar_image)  # returns "animated_avatar.mp4"
        voice_text = f"Introducing {product_name} - the best in its class."
        voice_file = generate_voice(voice_text)        # returns "voice.wav"
        synced_video = sync_lip(animated_video, voice_file)  # returns "synced_video.mp4"
        final_video = merge_video(voice_file, synced_video)   # returns "final_ad.mp4"
        
        return jsonify({
            "message": "Video ad generated successfully (test mode)",
            "video_url": final_video,
            "status": "success"
        })
    except Exception as e:
        print(f"Error: {str(e)}")  # Logs error in the console
        return jsonify({
            "message": "An error occurred while generating the ad",
            "error": str(e),
            "status": "error"
        }), 500

# Helper function for handling CORS preflight requests
def _handle_cors_preflight():
    response = jsonify({})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return response

# Placeholder helper functions – replace with actual integration later.
def generate_avatar(prompt):
    return "avatar.png"

def animate_avatar(avatar_image_path):
    return "animated_avatar.mp4"

def generate_voice(text):
    return "voice.wav"

def sync_lip(video_path, audio_path):
    return "synced_video.mp4"

def merge_video(audio_path, video_path):
    return "final_ad.mp4"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
