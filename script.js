document.addEventListener("DOMContentLoaded", function () {
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
        // Optionally, update your UI by setting the response into an element:
        // document.getElementById("result").innerText = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error("Error calling backend API:", error);
    });
});
