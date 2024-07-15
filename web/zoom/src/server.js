import WebSocket from "ws"
import http from "http"
import express from "express"

const app = express()

app.set("view engine", "pug")
app.set("views", __dirname + "/views")
app.use("/public", express.static(__dirname+"/public"))
app.get("/", (req,res) => res.render("home"))

const handleListen = () => console.log("now-localhost:3000")

// it's http server
const server = http.createServer(app)

// it's ws server
const wss = new WebSocket.Server({server})

const sockets = []

wss.on("connection", (socket) => {
    sockets.push(socket)
    socket.on("close", () => console.log("disconnected"))
    socket.on("message", (message) => {
        sockets.forEach(aSocket => aSocket.send(message.toString()))
        socket.send(message.toString())
    })
})

server.listen(3000, handleListen)