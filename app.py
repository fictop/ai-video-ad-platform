from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!"

# -----------------------------------------------------
# Helper Functions (Placeholders for actual implementation)
# -----------------------------------------------------

def generate_avatar(prompt):
    """
    Generate a realistic avatar image using Stable Diffusion.
    (Placeholder: Replace with code using Hugging Face diffusers)
    """
    # For now, assume a placeholder image file exists:
    return "avatar.png"

def animate_avatar(avatar_image_path):
    """
    Animate the static avatar image using a First Order Motion Model (FOMM).
    (Placeholder: Replace with actual animation code)
    """
    animated_video_path = "animated_avatar.mp4"
    return animated_video_path

def generate_voice(text):
    """
    Generate a voiceover using an open-source TTS engine (e.g., Coqui TTS).
    (Placeholder: Replace with actual TTS integration)
    """
    # For now, assume a placeholder audio file exists:
    return "voice.wav"

def sync_lip(video_path, audio_path):
    """
    Sync the avatar's lip movements with the generated voice using Wav2Lip.
    (Placeholder: Replace with actual Wav2Lip integration code)
    """
    output_synced = "synced_video.mp4"
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
    """
    Merge the synced video with audio using FFmpeg.
    (Placeholder: Adjust the FFmpeg command as necessary)
    """
    final_output = "final_ad.mp4"
    command = [
        "ffmpeg", "-y", "-i", video_path, "-i", audio_path,
        "-c:v", "copy", "-c:a", "aac", final_output
    ]
    subprocess.run(command, check=True)
    return final_output

# -----------------------------------------------------
# Main Endpoint: /create-ad with explicit OPTIONS handling
# -----------------------------------------------------

@app.route("/create-ad", methods=["POST", "OPTIONS"])
def create_ad():
    # Handle preflight OPTIONS request explicitly:
    if request.method == "OPTIONS":
        return jsonify({}), 200

    # Process POST request normally:
    data = request.json
    product_name = data.get("product_name", "Demo Product")
    prompt = data.get("prompt", "A professional avatar for advertisement")
    
    try:
        # Step 1: Generate avatar image based on the prompt
        avatar_image = generate_avatar(prompt)
        
        # Step 2: Animate the avatar (generate an animated video)
        animated_video = animate_avatar(avatar_image)
        
        # Step 3: Generate a voiceover using TTS
        voice_text = f"Introducing {product_name} - the best in its class."
        voice_file = generate_voice(voice_text)
        
        # Step 4: Sync lip movements with the generated voice using Wav2Lip
        synced_video = sync_lip(animated_video, voice_file)
        
        # Step 5: Merge the synced video with audio using FFmpeg
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

# -----------------------------------------------------
# Run the Flask App
# -----------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
