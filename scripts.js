fetch("https://api.fictop.com/generate-video", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ product_name: "Demo Product" })
})
.then(response => response.json())
.then(data => {
    console.log("API Response:", data);
})
.catch(error => {
    console.error("Error calling backend API:", error);
});
