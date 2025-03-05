from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

# Define the Flask app and enable CORS
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Home endpoint
@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!"

# (Optional) Existing /generate-video endpoint (if you want to keep it)
@app.route("/generate-video", methods=["POST", "OPTIONS"])
def generate_video():
    if request.method == "OPTIONS":
        return jsonify({}), 200

    data = request.json  
    product_name = data.get("product_name", "Unknown Product")
    return jsonify({"message": f"Generating video for {product_name}", "status": "success"})

# New integrated endpoint for creating an ad with the full AI pipeline
@app.route("/create-ad", methods=["POST", "OPTIONS"])
def create_ad():
    # Handle preflight OPTIONS request
    if request.method == "OPTIONS":
        return jsonify({}), 200

    data = request.json
    product_name = data.get("product_name", "Demo Product")
    prompt = data.get("prompt", "A professional avatar for advertisement")
    
    try:
        # Step 1: Generate avatar image based on the prompt (placeholder)
        avatar_image = generate_avatar(prompt)
        
        # Step 2: Animate the avatar (placeholder)
        animated_video = animate_avatar(avatar_image)
        
        # Step 3: Generate a voiceover using TTS (placeholder)
        voice_text = f"Introducing {product_name} - the best in its class."
        voice_file = generate_voice(voice_text)
        
        # Step 4: Sync lip movements with the generated voice using Wav2Lip (placeholder)
        synced_video = sync_lip(animated_video, voice_file)
        
        # Step 5: Merge the synced video with audio using FFmpeg (placeholder)
        final_video = merge_video(voice_file, synced_video)
        
        return jsonify({
            "message": "Video ad generated successfully",
            "video_url": final_video,
            "status": "success"
        })
    except Exception as e:
        return jsonify({
            "message": str(e),
            "status": "error"
        })

# Placeholder helper functions – these must be replaced with actual integration later.
def generate_avatar(prompt):
    # For now, return a placeholder image path
    return "avatar.png"

def animate_avatar(avatar_image_path):
    # For now, return a placeholder animated video path
    return "animated_avatar.mp4"

def generate_voice(text):
    # For now, return a placeholder audio file path
    return "voice.wav"

def sync_lip(video_path, audio_path):
    # For now, simulate lip syncing by returning a placeholder file path.
    output_synced = "synced_video.mp4"
    # Example command – in production, ensure that the Wav2Lip script and checkpoint exist.
    command = [
        "python", "Wav2Lip/inference.py",
        "--checkpoint_path", "Wav2Lip/checkpoints/wav2lip_gan.pth",
        "--face", video_path,
        "--audio", audio_path,
        "--outfile", output_synced
    ]
    subprocess.run(command, check=True)
    return output_synced

def merge_video(audio_path, video_path):
    final_output = "final_ad.mp4"
    # Example FFmpeg command – adjust as needed.
    command = [
        "ffmpeg", "-y", "-i", video_path, "-i", audio_path,
        "-c:v", "copy", "-c:a", "aac", final_output
    ]
    subprocess.run(command, check=True)
    return final_output

# Run the Flask app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
