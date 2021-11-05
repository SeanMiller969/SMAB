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
app.set("view engine", "pug");													/* pug is the engine used to display layouts */
app.use(express.static(path.join(__dirname, "public")));        /* Use public directory to store any images and css that frontend will use */

/**
 * Routes Definitions
 * Contains routes to each page with the information for its specific page
 */
app.get("/", (req, res) => {
  res.render("index", { title: "Home" });
});
app.get("/csgo-weapon-case", (req, res) => {
	res.render("csgo-weapon-case", { title: "CS:GO-Weapon-Case" });
});

app.get("/esports-2013-case", (req, res) => {
	res.render("esports-2013-case", { title: "eSports 2013 Case" });
});

app.get("/operation-bravo-case", (req, res) => {
	res.render("operation-bravo-case", { title: "Operation Bravo Case" });
});

app.get("/csgo-weapon-case-2", (req, res) => {
	res.render("csgo-weapon-case-2", { title: "CS:GO Weapon Case 2" });
});

app.get("/esports-2013-winter-case", (req, res) => {
	res.render("esports-2013-winter-case", { title: "eSports 2013 Winter Case" });
});

app.get("/winter-offensive-weapon-case", (req, res) => {
	res.render("winter-offensive-weapon-case", { title: "Winter Offensive Weapon Case" });
});

app.get("/csgo-weapon-case-3", (req, res) => {
	res.render("csgo-weapon-case-3", { title: "CS:GO Weapon Case 3" });
});

app.get("/operation-phoenix-weapon-case", (req, res) => {
	res.render("operation-phoenix-weapon-case", { title: "Operation Phoenix Weapon Case" });
});

app.get("/huntsman-weapon-case", (req, res) => {
	res.render("huntsman-weapon-case", { title: "Huntsman Weapon Case" });
});

app.get("/operation-breakout-weapon-case", (req, res) => {
	res.render("operation-breakout-weapon-case", { title: "Operation Breakout Weapon Case" });
});

app.get("/esports-2014-summer-case", (req, res) => {
	res.render("esports-2014-summer-case", { title: "eSports 2014 Summer Case" });
});

app.get("/operation-vanguard-weapon-case", (req, res) => {
	res.render("operation-vanguard-weapon-case", { title: "Operation Vanguard Weapon Case" });
});

app.get("/chroma-case", (req, res) => {
	res.render("chroma-case", { title: "Chroma Case" });
});

app.get("/chroma-2-case", (req, res) => {
	res.render("chroma-2-case", { title: "Chroma 2 Case" });
});

app.get("/falchion-case", (req, res) => {
	res.render("falchion-case", { title: "Falchion Case" });
});

app.get("/shadow-case", (req, res) => {
	res.render("shadow-case", { title: "Shadow Case" });
});

app.get("/revolver-case", (req, res) => {
	res.render("revolver-case", { title: "Revolver Case" });
});

app.get("/operation-wildfire-case", (req, res) => {
	res.render("operation-wildfire-case", { title: "Operation Wildfire Case" });
});

app.get("/chroma-3-case", (req, res) => {
	res.render("chroma-3-case", { title: "Chroma 3 Case" });
});

app.get("/gamma-case", (req, res) => {
	res.render("gamma-case", { title: "Gamma Case" });
});

app.get("/gamma-2-case", (req, res) => {
	res.render("gamma-2-case", { title: "Gamma 2 Case" });
});

app.get("/glove-case", (req, res) => {
	res.render("glove-case", { title: "Glove Case" });
});

app.get("/spectrum-case", (req, res) => {
	res.render("spectrum-case", { title: "Spectrum Case" });
});

app.get("/operation-hydra-case", (req, res) => {
	res.render("operation-hydra-case", { title: "Operation Hydra Case" });
});

app.get("/spectrum-2-case", (req, res) => {
	res.render("spectrum-2-case", { title: "Spectrum 2 Case" });
});

app.get("/clutch-case", (req, res) => {
	res.render("clutch-case", { title: "Clutch Case" });
});

app.get("/horizon-case", (req, res) => {
	res.render("horizon-case", { title: "Horizon Case" });
});

app.get("/danger-zone-case", (req, res) => {
	res.render("danger-zone-case", { title: "Danger Zone Case" });
});

app.get("/prisma-case", (req, res) => {
	res.render("prisma-case", { title: "Prisma Case" });
});

app.get("/cs20-case", (req, res) => {
	res.render("cs20-case", { title: "CS20 Case" });
});

app.get("/shattered-web-case", (req, res) => {
	res.render("shattered-web-case", { title: "Shattered Web Case" });
});

app.get("/prisma-2-case", (req, res) => {
	res.render("prisma-2-case", { title: "Prisma 2 Case" });
});

app.get("/fracture-case", (req, res) => {
	res.render("fracture-case", { title: "Fracture Case" });
});

app.get("/operation-broken-fang-case", (req, res) => {
	res.render("operation-broken-fang-case", { title: "Operation Broken Fang Case" });
});

app.get("/snakebite-case", (req, res) => {
	res.render("snakebite-case", { title: "Snakebite Case" });
});

app.get("/operation-riptide-case", (req, res) => {
	res.render("operation-riptide-case", { title: "Operation Riptide Case" });
});

/**
 * Server Activation
 */
app.listen(port, () => {
  console.log(`Listening to requests on http://localhost:${port}`);
});