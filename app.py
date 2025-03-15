from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import subprocess  # Import subprocess to run FFmpeg

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!", 200

@app.route("/generate-video", methods=["POST", "OPTIONS"])
def generate_video():
    if request.method == "OPTIONS":
        return _handle_cors_preflight()
    data = request.get_json(silent=True) or {}
    product_name = data.get("product_name", "Unknown Product")
    return jsonify({"message": f"Generating video for {product_name}", "status": "success"})

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
        # Step 1: Generate avatar image using Stable Diffusion (CPU-only)
        avatar_image = generate_avatar(prompt)
        
        # Step 2: Animate avatar (placeholder)
        animated_video = animate_avatar(avatar_image)
        
        # Step 3: Generate voice file (placeholder)
        voice_file = generate_voice(f"Introducing {product_name} - the best in its class.")
        
        # Step 4: Sync lip movements (placeholder)
        synced_video = sync_lip(animated_video, voice_file)
        
        # Step 5: Merge video and audio (placeholder)
        merged_video = merge_video(voice_file, synced_video)

        # Step 6: Apply our custom watermark using FFmpeg
        final_video = apply_watermark(merged_video)

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

def _handle_cors_preflight():
    response = jsonify({})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return response

def generate_avatar(prompt):
    from diffusers import StableDiffusionPipeline
    import torch

    # Create a writable cache directory
    cache_dir = "./.cache"
    os.makedirs(cache_dir, exist_ok=True)

    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cpu"  # Force CPU mode
    pipe = StableDiffusionPipeline.from_pretrained(model_id, safety_checker=None, cache_dir=cache_dir).to(device)
    result = pipe(prompt, guidance_scale=7.5)
    image = result.images[0]
    output_path = "avatar.png"
    image.save(output_path)
    return output_path

def animate_avatar(avatar_path):
    # Placeholder: Return a dummy filename
    return "animated_avatar.mp4"

def generate_voice(text):
    # Placeholder: Return a dummy filename
    return "voice.wav"

def sync_lip(video_path, audio_path):
    # Placeholder: Return a dummy filename
    return "synced_video.mp4"

def merge_video(audio_path, video_path):
    # For testing, return a dummy merged video file name.
    # In a real scenario, this would merge the audio and video files.
    return "sample.mp4"

def apply_watermark(input_video, watermark_path="watermark.png", output_video="final_video.mp4"):
    """
    Overlays a custom watermark onto the video using FFmpeg.
    - input_video: path to the merged video (without watermark)
    - watermark_path: path to your custom watermark image
    - output_video: path where the watermarked video will be saved
    """
    # Construct the FFmpeg command
    command = [
        "ffmpeg",
        "-i", input_video,
        "-i", watermark_path,
        "-filter_complex", "overlay=10:10",  # Adjust the position (x=10, y=10)
        "-codec:a", "copy",  # Copy audio without re-encoding
        output_video
    ]
    # Run the FFmpeg command
    subprocess.run(command, check=True)
    return output_video

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
