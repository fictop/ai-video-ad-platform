fetch("https://raw.githubusercontent.com/fictop/ai-video-ad-platform/main/meta.json")
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("meta.json loaded successfully:", data);
    })
    .catch(error => {
        console.error("Error loading meta.json:", error);
    });
