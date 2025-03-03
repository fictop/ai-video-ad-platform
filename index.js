const express = require("express");
const app = express();

app.use(express.static("public")); // Serves static files from 'public' folder

app.get("/", (req, res) => {
    res.send("AI Video Ad Platform is running!");
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
