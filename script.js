document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM fully loaded and parsed");

    // Attach click event to the "Get Started" button
    const createAdBtn = document.getElementById("createAdBtn");
    if (!createAdBtn) {
        console.error("Button with id 'createAdBtn' not found");
        return;
    }

    createAdBtn.addEventListener("click", function () {
        console.log("Get Started button clicked");

        // Send a POST request to your backend's /create-ad endpoint
        fetch("https://api.fictop.com/create-ad", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                product_name: "Demo Product",
                prompt: "A futuristic professional avatar for advertisement"
            })
        })
        .then(response => {
            console.log("Response received from backend");
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("API Response:", data);

            // Update the result div with the API response
            const resultElement = document.getElementById("result");
            if (resultElement) {
                resultElement.innerText = JSON.stringify(data, null, 2);
            } else {
                console.warn("Result element not found");
            }

            // If a video URL is returned, update and show the video player
            if (data.video_url) {
                const videoElement = document.getElementById("videoPlayer");
                const videoSource = document.getElementById("videoSource");

                // If the URL is relative (like "final_ad.mp4"), prepend the GitHub Pages URL
                if (!data.video_url.startsWith("http")) {
                    videoSource.src = "https://fictop.github.io/ai-video-ad-platform/" + data.video_url;
                    console.log("Set video source to:", videoSource.src);
                } else {
                    videoSource.src = data.video_url;
                }
                videoElement.load(); // Reload video source
                videoElement.style.display = "block"; // Show the video player
            }
        })
        .catch(error => {
            console.error("Error calling backend API:", error);
            const resultElement = document.getElementById("result");
            if (resultElement) {
                resultElement.innerText = "Error: " + error;
            }
        });
    });
});
