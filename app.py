from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
import tempfile
from diffusers import StableDiffusionPipeline
import torch

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global configuration
MODEL_ID = "runwayml/stable-diffusion-v1-5"  # More optimized model
MAX_PROMPT_LENGTH = 200
ALLOWED_MIME_TYPES = {'image/png', 'video/mp4'}

@app.route("/")
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "active",
        "service": "AI Video Ad Platform",
        "version": "1.0.0"
    }), 200

@app.route("/generate-ad", methods=["POST"])
def create_ad():
    """Main endpoint for ad generation"""
    try:
        # Validate input
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
            
        product_name = data.get("product_name", "Our Product")
        prompt = data.get("prompt", "professional product advertisement")
        
        if len(prompt) > MAX_PROMPT_LENGTH:
            return jsonify({"error": f"Prompt exceeds {MAX_PROMPT_LENGTH} characters"}), 400

        # Create temporary workspace
        with tempfile.TemporaryDirectory() as workspace:
            # Generate assets
            avatar_path = generate_avatar(prompt, workspace)
            
            # For demo purposes - replace with actual processing
            response_data = {
                "status": "success",
                "product": product_name,
                "avatar": os.path.basename(avatar_path),
                "message": "Demo generation complete - implement remaining steps"
            }

            return jsonify(response_data)

    except Exception as e:
        logger.error(f"Generation failed: {str(e)}", exc_info=True)
        return jsonify({
            "status": "error",
            "message": "Ad generation failed",
            "error": str(e)
        }), 500

def generate_avatar(prompt, output_dir):
    """Generate avatar image with optimized settings"""
    try:
        # Initialize pipeline
        pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float32,  # Required for CPU
            safety_checker=None,
            use_safetensors=True
        ).to("cpu")

        # Optimized settings for CPU
        result = pipe(
            prompt,
            num_inference_steps=25,
            guidance_scale=7.5,
            height=512,
            width=512
        )

        # Save output
        output_path = os.path.join(output_dir, "generated_avatar.png")
        result.images[0].save(output_path)
        logger.info(f"Avatar generated: {output_path}")
        
        return output_path

    except Exception as e:
        logger.error(f"Avatar generation failed: {str(e)}")
        raise

# Temporary placeholder implementations
def animate_avatar(avatar_path):
    """Placeholder for animation logic"""
    return f"animated_{os.path.basename(avatar_path)}"

def generate_voice(text):
    """Placeholder for voice generation"""
    return "generated_voice.wav"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, threaded=False)  # Disable threading for stability
