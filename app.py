from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
import tempfile
from diffusers import StableDiffusionPipeline
import torch

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# For demonstration, using a smaller or more optimized model can reduce build size
MODEL_ID = "runwayml/stable-diffusion-v1-5"
MAX_PROMPT_LENGTH = 200

@app.route("/")
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "active",
        "service": "AI Video Ad Platform",
        "version": "1.0.0"
    }), 200

@app.route("/generate-ad", methods=["POST", "OPTIONS"])
def create_ad():
    """
    Main endpoint for ad generation.
    This version uses CPU-only stable diffusion to reduce memory usage.
    """
    try:
        if request.method == "OPTIONS":
            return _handle_cors_preflight()

        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        product_name = data.get("product_name", "Our Product")
        prompt = data.get("prompt", "professional product advertisement")

        # Validate prompt length
        if len(prompt) > MAX_PROMPT_LENGTH:
            return jsonify({
                "error": f"Prompt exceeds {MAX_PROMPT_LENGTH} characters"
            }), 400

        # Use a temporary directory for generated files
        with tempfile.TemporaryDirectory() as workspace:
            avatar_path = generate_avatar(prompt, workspace)

            # Placeholder for further steps (animation, voice, etc.)
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
    """
    Generate an avatar image using CPU-based Stable Diffusion.
    Saves the output in output_dir as 'generated_avatar.png'.
    """
    try:
        # Force CPU usage
        device = "cpu"
        # Load the pipeline
        pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float32,
            safety_checker=None,
            use_safetensors=True
        ).to(device)

        # Generate image with fewer steps to reduce time
        result = pipe(
            prompt,
            num_inference_steps=25,
            guidance_scale=7.5,
            height=512,
            width=512
        )

        output_path = os.path.join(output_dir, "generated_avatar.png")
        result.images[0].save(output_path)
        logger.info(f"Avatar generated: {output_path}")
        return output_path

    except Exception as e:
        logger.error(f"Avatar generation failed: {str(e)}")
        raise

def _handle_cors_preflight():
    """Handle CORS preflight requests."""
    response = jsonify({})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return response

if __name__ == "__main__":
    # Choreo often sets PORT=8000 by default
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, threaded=False)
