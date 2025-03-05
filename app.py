@app.route("/create-ad", methods=["POST", "OPTIONS"])
def create_ad():
    # Handle preflight OPTIONS request explicitly:
    if request.method == "OPTIONS":
        return jsonify({}), 200

    data = request.json
    product_name = data.get("product_name", "Demo Product")
    prompt = data.get("prompt", "A professional avatar for advertisement")

    try:
        # Step 1: Generate avatar image (placeholder)
        avatar_image = generate_avatar(prompt)  # Returns "avatar.png"
        
        # Step 2: Animate avatar (placeholder)
        animated_video = animate_avatar(avatar_image)  # Returns "animated_avatar.mp4"
        
        # Step 3: Generate voiceover (placeholder)
        voice_text = f"Introducing {product_name} - the best in its class."
        voice_file = generate_voice(voice_text)  # Returns "voice.wav"
        
        # For testing, skip syncing and merging:
        final_video = animated_video  # Use the animated video as a placeholder
        
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
