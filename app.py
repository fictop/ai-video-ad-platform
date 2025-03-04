from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Video Ad Platform Backend is Running!"

@app.route("/generate-video", methods=["POST"])
def generate_video():
    data = request.json  # Get product details from frontend
    product_name = data.get("product_name", "Unknown Product")
    
    # Placeholder response (Replace with AI video generation logic)
    return jsonify({"message": f"Generating video for {product_name}", "status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
