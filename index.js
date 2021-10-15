// index.js

/**
 * Required External Modules
 */
const express = require("express");
const path = require("path");

/**
 * App Variables
 */
const app = express();
const port = process.env.PORT || "8000";

/**
 *  App Configuration
 */
app.set("views", path.join(__dirname, "views"));				/* Views directory will store pug templates for frontend layout */
app.set("view engine", "pug");									/* pug is the engine used to display layouts */
app.use(express.static(path.join(__dirname, "public")));        /* Use public directory to store any images and css that frontend will use */

/**
 * Routes Definitions
 */
app.get("/", (req, res) => {
  res.render("index", { title: "Home" });
});

/**
 * Server Activation
 */
app.listen(port, () => {
  console.log(`Listening to requests on http://localhost:${port}`);
});