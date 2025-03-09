from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# Initialize the Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Home endpoint to check if the backend is running
@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!", 200

# Optional endpoint for generating a video (placeholder)
@app.route("/generate-video", methods=["POST", "OPTIONS"])
def generate_video():
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    data = request.json or {}
    product_name = data.get("product_name", "Unknown Product")
    return jsonify({"message": f"Generating video for {product_name}", "status": "success"})

# Main endpoint for creating an ad using the full AI pipeline
@app.route("/create-ad", methods=["POST", "OPTIONS", "GET"])
def create_ad():
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    if request.method == "GET":
        return jsonify({"message": "Please use POST to create an ad", "status": "error"}), 405

    data = request.json or {}
    product_name = data.get("product_name", "Demo Product")
    prompt = data.get("prompt", "A professional avatar for advertisement")
    
    try:
        # Step 1: Generate an avatar image using Stable Diffusion
        avatar_image = generate_avatar(prompt)       # returns "avatar.png"
        
        # Step 2: Animate the avatar (placeholder)
        animated_video = animate_avatar(avatar_image)  # returns "animated_avatar.mp4"
        
        # Step 3: Generate a voiceover (placeholder)
        voice_text = f"Introducing {product_name} - the best in its class."
        voice_file = generate_voice(voice_text)        # returns "voice.wav"
        
        # Step 4: Sync lip movements (placeholder)
        synced_video = sync_lip(animated_video, voice_file)  # returns "synced_video.mp4"
        
        # Step 5: Merge video and audio (placeholder)
        final_video = merge_video(voice_file, synced_video)   # returns "final_ad.mp4"
        
        return jsonify({
            "message": "Video ad generated successfully (test mode)",
            "video_url": final_video,
            "status": "success"
        })
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            "message": "An error occurred while generating the ad",
            "error": str(e),
            "status": "error"
        }), 500

# Helper function for handling CORS preflight requests
def _handle_cors_preflight():
    response = jsonify({})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return response

# Function to generate an avatar image using Stable Diffusion
def generate_avatar(prompt):
    from diffusers import StableDiffusionPipeline
    import torch

    model_id = "CompVis/stable-diffusion-v1-4"
    
    # Force CPU mode
    device = "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, safety_checker=None  # Fix for some hosting issues
    ).to(device)
    
    result = pipe(prompt, guidance_scale=7.5)
    image = result.images[0]
    
    output_path = "avatar.png"
    image.save(output_path)
    return output_path

# Placeholder functions for further processing
def animate_avatar(avatar_image_path):
    return "animated_avatar.mp4"

def generate_voice(text):
    return "voice.wav"

def sync_lip(video_path, audio_path):
    return "synced_video.mp4"

def merge_video(audio_path, video_path):
    return "final_ad.mp4"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
