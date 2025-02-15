import express from "express";
import cors from "cors";
require("dotenv").config();
import router from "./routes/router";
const app = express();
app.use(cors());
app.use(express.json());
app.use("/api", router);


app.get("/test", (req, res) => {
  res.send("Node.js Backend is Running!");
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});