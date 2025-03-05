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
.then(response => response.json())
.then(data => {
    console.log("API Response:", data);
})
.catch(error => {
    console.error("Error calling backend API:", error);
});
