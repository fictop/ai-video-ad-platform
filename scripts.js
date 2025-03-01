fetch("meta.json")
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log("meta.json loaded successfully:", data);
    // Do something with the data if needed.
  })
  .catch(error => {
    console.error("Error loading meta.json:", error);
  });
