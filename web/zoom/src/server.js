// import WebSocket from "ws"
import http from "http"
import express from "express"
import SocketIO from "socket.io"

const app = express()

app.set("view engine", "pug")
app.set("views", __dirname + "/views")
app.use("/public", express.static(__dirname+"/public"))
app.get("/", (req,res) => res.render("home"))


const httpServer = http.createServer(app)
// noinspection JSValidateTypes
const wsServer = SocketIO(httpServer)

function publicRooms() {
    const {sids, rooms} = wsServer.sockets.adapter;

    const publicRooms = [];
    rooms.forEach((_,key) => {
        if (sids.get(key) === undefined) {
            publicRooms.push(key)
        }
    })
    return publicRooms;
}

function countRoom(roomName) {
    return wsServer.socket.adapter.rooms.get(roomName)?.size
}

wsServer.on("connection", socket => {
    socket["nickname"] = socket.id
    // 뭐든 이벤트가 일어나면 실행
    socket.onAny((event) => {
        console.log(`Socket Event: ${event}`)
    })

    socket.on("enterRoom", (roomName, done) => {
        socket.join(roomName)
        done() // it's function from FE
        socket.to(roomName).emit("welcome", socket.nickname)
        wsServer.sockets.emit("room_change", publicRooms())
    })

    socket.on("disconnecting", () => {
        socket.rooms.forEach((room) =>
            socket.to(room).emit("bye", socket.nickname)
        )
    })

    socket.on("disconnect", () => {
        wsServer.sockets.emit("room_change", publicRooms())
    })

    socket.on("new_message", (msg, room, done) => {
        socket.to(room).emit("new_message", `${socket.nickname}: ${msg}`)
        done()
    })

    socket.on("nickname", nickname => socket["nickname"] = nickname)
    })









// with ws way
// it's ws server
// const wss = new WebSocket.Server({server})
// const sockets = []
//
// wss.on("connection", (socket) => {
//     sockets.push(socket)
//     // 소켓이 들어오면서 기본 닉네임을 설정
//     socket["nickname"] = "Anonymous"
//     socket.on("close", () => console.log("disconnected"))
//     socket.on("message", (msg) => {
//         const message = JSON.parse(msg)
//         // 메세지의 타입을 구분
//         switch(message.type) {
//             // 메시지 칸에서 들어온 경우
//             case "new_message":
//                 sockets.forEach(aSocket => aSocket.send(`${socket.nickname}: ${message.payload}`))
//                 return
//             // 닉네임 칸에서 들어온 경우
//             case "nickname":
//                 socket["nickname"] = message.payload
//                 return
//         }
//     })
// })

httpServer.listen(3000)
