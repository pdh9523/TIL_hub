const socket = io()

const welcome = document.getElementById("welcome")
const room = document.getElementById("room")
const enterRoom = welcome.querySelector("#enter-room")
const nickname = welcome.querySelector("#nickname")
// 닉네임 설정 검증용
let check = false

room.hidden = true
let roomName;
// 방 설정
/**
 * 방을 생성하는 경우 enterRoom의 eventListener에 반응하는 함수
 *
 * @param {Object} event 이벤트 리스너를 통해 받아오는 이벤트
 *
 * @return 없음
 */

function handleRoomSubmit(event) {
    event.preventDefault()
    const input = enterRoom.querySelector("input")
    if (check) {
    socket.emit("enterRoom", input.value, showRoom)
    roomName = input.value
    input.value = ""
    } else {
        window.alert("닉네임을 설정해주세요")
    }
}
// 닉네임 설정
function handleNickNameSubmit(event) {
    check = true
    event.preventDefault()
    const input = welcome.querySelector("#nickname input")
    if (window.confirm("이 닉네임을 사용하시겠습니까?")) {
        socket.emit("nickname", input.value)
        window.alert(`당신의 닉네임은 ${input.value}입니다.`)
    }
}

nickname.addEventListener("submit", handleNickNameSubmit)
enterRoom.addEventListener("submit", handleRoomSubmit)

// 방 진입
function showRoom() {
    welcome.hidden = true
    room.hidden = false
    const h3 = room.querySelector("h3")
    h3.innerText = roomName
    const msg = room.querySelector("#message")
    msg.addEventListener("submit", handleMessageSubmit)
}

// 메시지 입력
function handleMessageSubmit(event) {
    event.preventDefault()
    const input = room.querySelector("#message input")
    const value = input.value
    socket.emit("new_message", input.value, roomName, () => {
        addMessage (`you: ${value}`)
    })
    input.value = ""
}
// 메시지 출력
function addMessage(msg) {
    const ul = room.querySelector("ul")
    const li = document.createElement("li")
    li.innerText = msg
    ul.appendChild(li)
}

socket.on("welcome", (user) => {
    addMessage(`${user}님이 입장 하셨습니다.`)
})

// socket.on("new_message", (msg) => {
//     addMessage("new_message", (msg) => addMessage(msg))
// })
// 위와 동일
socket.on("new_message", addMessage)

socket.on("bye", (user) => {
    addMessage(`${user}님이 퇴장 하셨습니다.`)
})
