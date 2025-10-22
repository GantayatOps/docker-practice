const express = require("express");
const mongoose = require("mongoose");

const app = express();

mongoose.connect("mongodb://mongo:27017/testdb", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on("error", console.error.bind(console, "MongoDB connection error:"));
db.once("open", () => console.log("✅ Connected to MongoDB"));

app.get("/", (req, res) => {
  res.send("Hello from Node + MongoDB!");
});

app.listen(3000, () => console.log("🚀 Server running on port 3000"));