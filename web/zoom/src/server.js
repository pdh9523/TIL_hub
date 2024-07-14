import WebSocket from "ws"
import http from "http"
import express from "express"

const app = express()

app.set("view engine", "pug")
app.set("views", __dirname + "/views")
app.use("/public", express.static(__dirname+"/public"))
app.get("/", (req,res) => res.render("home"))

const handleListen = () => console.log("Hello")

// it's http server
const server = http.createServer(app)

// it's ws server
const wss = new WebSocket.Server({server})

function handleConnection(socket) {
    console.log(socket)
}

wss.on("connection", handleConnection)

server.listen(3000, handleListen)