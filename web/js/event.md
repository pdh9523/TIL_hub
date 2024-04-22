# Event
무언가 일어났다는 신호나 사건을 말하며, 모든 DOM 요소는 이러한 event를 만들어낸다.

DOM 요소는 event를 받고 받은 event를 event handler를 통해 처리할 수 있다. 

## Event handler
이벤트가 발생했을 때 실행되는 함수로, 사용자의 행동에 어떻게 반응할지를 JS 코드로 표현한 것이다. 

### `.addEventListener()`
대표적인 이벤트 핸들러 중 하나로, 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출한다.

`EventTarget.addEventListener(type, handler)`
대상에 특정 Event가 발생하면, 지정한 이벤트를 받아 할 일을 등록한다 .

```js
// 1 . 버튼 선택
const btn = document.querySelector('#btn')
// 2. 콜백 함수
const detectClick = function (event) {
  console.log(event)  // PointerEvent
  console.log(event.currentTarget)  // <button id='btn> 버튼</button>'
  console.log(this)  // <button id='btn> 버튼</button>'
}
// 3. 버튼에 이벤트 핸들러를 부착
btn.addEvnetListener('click', detectClick)

```

## 버블링

한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상.

가장 최상단의 조상 요소를 만날 때까지 이 과정에 반복되면서 요소 각각에 할당된 핸들러가 동작

### 해결방법

### `currentTarget`
'현재' 요소를 선택.

항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성으로, this와 같다.

### `target`
이벤트가 발생한 가장 안쪽의 요소를 참조하는 속성으로, 실제 이벤트가 시작된 요소이며, 버블링이 진행되어도 변하지 않는다. 