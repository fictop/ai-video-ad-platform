document.addEventListener("DOMContentLoaded", function () {
    // Attach event listener to the "Get Started" button
    document.getElementById("createAdBtn").addEventListener("click", function () {
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
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("API Response:", data);
            // Update the result div with the response data
            const resultElement = document.getElementById("result");
            resultElement.innerText = JSON.stringify(data, null, 2);
            // If a video URL is returned, update and show the video player
            if (data.video_url) {
                const videoElement = document.getElementById("videoPlayer");
                // If the returned URL is relative, prepend the GitHub raw URL
                if (!data.video_url.startsWith("http")) {
                    videoElement.src = "https://raw.githubusercontent.com/fictop/ai-video-ad-platform/main/" + data.video_url;
                } else {
                    videoElement.src = data.video_url;
                }
                videoElement.style.display = "block"; // Make the video player visible
            }
        })
        .catch(error => {
            console.error("Error calling backend API:", error);
            document.getElementById("result").innerText = "Error: " + error;
        });
    });
});
