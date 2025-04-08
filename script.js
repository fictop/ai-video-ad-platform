document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM fully loaded and parsed");

    const createAdBtn = document.getElementById("createAdBtn");
    if (!createAdBtn) {
        console.error("Button with id 'createAdBtn' not found");
        return;
    }

    createAdBtn.addEventListener("click", function () {
        console.log("Get Started button clicked");

        // IMPORTANT: Use your Render backend URL exactly
        fetch("https://ai-video-backend-bnp9.onrender.com/create-ad", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                product_name: "Demo Product",
                prompt: "A futuristic AI ad"
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`API request failed with status ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("API Response:", data);

            if (data.video_url) {
                const videoElement = document.getElementById("videoPlayer");
                const videoSource = document.getElementById("videoSource");

                // Set the video source to the returned URL
                videoSource.src = data.video_url;
                videoElement.load();

                // Make sure the video is visible
                videoElement.style.display = "block";

                // Attempt to play the video automatically
                videoElement.oncanplay = function () {
                    videoElement.play()
                        .then(() => console.log("Playing video:", data.video_url))
                        .catch(err => {
                            console.error("Error playing video:", err);
                            alert("Your browser may be blocking autoplay. Click on the video to play.");
                        });
                };
            } else {
                console.error("No video URL found in API response");
            }
        })
        .catch(error => console.error("Error calling backend API:", error));
    });
});
