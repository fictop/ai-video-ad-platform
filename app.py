from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import torch
from diffusers import StableDiffusionPipeline

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Home endpoint
@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!", 200

# Video generation endpoint
@app.route("/generate-video", methods=["POST", "OPTIONS"])
def generate_video():
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    data = request.json or {}
    product_name = data.get("product_name", "Unknown Product")
    return jsonify({"message": f"Generating video for {product_name}", "status": "success"})

# AI Ad generation endpoint
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
        print(f"Error: {str(e)}")
        return jsonify({
            "message": "An error occurred while generating the ad",
            "error": str(e),
            "status": "error"
        }), 500

# CORS Preflight Handler
def _handle_cors_preflight():
    response = jsonify({})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return response

# Generate Avatar using Stable Diffusion
def generate_avatar(prompt):
    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load model
    pipe = StableDiffusionPipeline.from_pretrained(model_id)
    pipe = pipe.to(device)

    # Generate image
    result = pipe(prompt, guidance_scale=7.5)
    image = result.images[0]

    # Save image
    output_path = "avatar.png"
    image.save(output_path)
    return output_path

# Placeholder Functions
def animate_avatar(avatar_image_path):
    return "animated_avatar.mp4"

def generate_voice(text):
    return "voice.wav"

def sync_lip(video_path, audio_path):
    return "synced_video.mp4"

def merge_video(audio_path, video_path):
    return "final_ad.mp4"

# Ensure Gunicorn can find the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
