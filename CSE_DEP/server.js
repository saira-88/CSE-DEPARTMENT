const express = require("express");
const path = require("path");

const app = express();
const PORT = 5000;

// Serve static files
app.use(express.static(path.join(__dirname, "public")));

// Example API
app.get("/api/faculty", (req, res) => {
    res.json([
        { name: "Dr. A Kumar", area: "AI" },
        { name: "Dr. B Rao", area: "Cyber Security" }
    ]);
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});