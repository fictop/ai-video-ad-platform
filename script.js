document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM fully loaded and parsed");

    const createAdBtn = document.getElementById("createAdBtn");
    if (!createAdBtn) {
        console.error("Button with id 'createAdBtn' not found");
        return;
    }

    createAdBtn.addEventListener("click", function () {
        console.log("Get Started button clicked");

        fetch("https://outstanding-vin-fictop-782bb985.koyeb.app/create-ad", {
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
                
                // Always make the video visible
                videoElement.style.display = "block";

                // Attempt to play the video
                videoElement.oncanplay = function () {
                    videoElement.play()
                        .then(() => console.log("Playing video:", data.video_url))
                        .catch(err => console.error("Error playing video:", err));
                };
            } else {
                console.error("No video URL found in API response");
            }
        })
        .catch(error => console.error("Error calling backend API:", error));
    });
});
