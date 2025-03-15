import os
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

# Force Hugging Face to store cache in /tmp (a writable directory)
os.environ["TRANSFORMERS_CACHE"] = "/tmp/huggingface_cache"
os.environ["HF_HOME"] = "/tmp/huggingface_cache"
os.makedirs("/tmp/huggingface_cache", exist_ok=True)

app = Flask(__name__)
CORS(app)
# Allow routes with or without trailing slash
app.url_map.strict_slashes = False

@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!", 200

# Simple test endpoint to verify routing
@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Test endpoint is working!"}), 200

@app.route("/create-ad", methods=["POST", "OPTIONS", "GET"])
def create_ad():
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    if request.method == "GET":
        return jsonify({"message": "Please use POST to create an ad", "status": "error"}), 405

    data = request.get_json(silent=True) or {}
    product_name = data.get("product_name", "Demo Product")
    prompt = data.get("prompt", "A professional avatar for advertisement")

    try:
        # Step 1: Generate avatar image using Stable Diffusion
        avatar_image = generate_avatar(prompt)

        # Step 2: Generate voice file using Coqui TTS
        voice_file = generate_voice(f"Introducing {product_name} - the best in its class.")

        # Step 3: Animate avatar with lip-sync using SadTalker
        animated_video = animate_avatar(avatar_image, voice_file)

        # Step 4: Apply custom watermark using FFmpeg
        final_video = apply_watermark(animated_video)

        return jsonify({
            "message": "Video ad generated successfully",
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

def _handle_cors_preflight():
    response = jsonify({})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return response

def generate_avatar(prompt):
    from diffusers import StableDiffusionPipeline
    import torch

    cache_dir = "./.cache"
    os.makedirs(cache_dir, exist_ok=True)

    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, safety_checker=None, cache_dir=cache_dir).to(device)
    result = pipe(prompt, guidance_scale=7.5)
    image = result.images[0]
    output_path = "avatar.png"
    image.save(output_path)
    return output_path

def generate_voice(text):
    from TTS.api import TTS
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
    output_path = "voice.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path

def animate_avatar(avatar_path, voice_path):
    output_video = "animated_avatar.mp4"
    command = [
        "python", "sadtalker.py",  # Ensure sadtalker.py is correctly in your project
        "--avatar", avatar_path,
        "--audio", voice_path,
        "--output", output_video
    ]
    subprocess.run(command, check=True)
    return output_video

def apply_watermark(input_video, watermark_path="watermark.png", output_video="final_video.mp4"):
    command = [
        "ffmpeg",
        "-i", input_video,
        "-i", watermark_path,
        "-filter_complex", "overlay=10:10",  # Adjust the position if needed
        "-codec:a", "copy",
        output_video
    ]
    subprocess.run(command, check=True)
    return output_video

# Remove the local app.run block so Gunicorn (from your Dockerfile) handles serving
