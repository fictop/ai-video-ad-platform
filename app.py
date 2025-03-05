from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!"

@app.route("/create-ad", methods=["POST", "OPTIONS"])
def create_ad():
    # Handle preflight OPTIONS request explicitly
    if request.method == "OPTIONS":
        return jsonify({}), 200

    data = request.json
    product_name = data.get("product_name", "Demo Product")
    prompt = data.get("prompt", "A professional avatar for advertisement")
    
    try:
        # Step 1: Generate avatar image (placeholder)
        avatar_image = generate_avatar(prompt)  # returns "avatar.png"
        
        # Step 2: Animate the avatar (placeholder)
        animated_video = animate_avatar(avatar_image)  # returns "animated_avatar.mp4"
        
        # Step 3: Generate a voiceover (placeholder)
        voice_text = f"Introducing {product_name} - the best in its class."
        voice_file = generate_voice(voice_text)  # returns "voice.wav"
        
        # Step 4: Sync lip movements (placeholder, no subprocess call)
        synced_video = "synced_video.mp4"
        
        # Step 5: Merge video with audio (placeholder, no subprocess call)
        final_video = "final_ad.mp4"
        
        return jsonify({
            "message": "Video ad generated successfully (test mode)",
            "video_url": final_video,
            "status": "success"
        })
    except Exception as e:
        return jsonify({
            "message": str(e),
            "status": "error"
        })

# Placeholder helper functions
def generate_avatar(prompt):
    # Return a placeholder image file path
    return "avatar.png"

def animate_avatar(avatar_image_path):
    # Return a placeholder animated video file path
    return "animated_avatar.mp4"

def generate_voice(text):
    # Return a placeholder audio file path
    return "voice.wav"

# For now, these functions simply return placeholder filenames.
def sync_lip(video_path, audio_path):
    return "synced_video.mp4"

def merge_video(audio_path, video_path):
    return "final_ad.mp4"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
