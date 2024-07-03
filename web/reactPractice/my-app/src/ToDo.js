import {useState, useEffect} from "react"

function App() {
  const [toDo, setToDo] = useState("");
  const [toDos, setToDos] = useState([]);

  const onChange = function(event) {
    setToDo(event.target.value);
  }

  const onSubmit = (event) => {
    // form의 기본값을 초기화 하기 위해서 preventDefault를 설정해줘야한다.
    event.preventDefault()
    if (toDo === "") {
      return
    }
    // useState로 배열을 선언하고 관리하기 위해서는 이런 방식을 사용할 수 있다.
    setToDos(currentArray => [toDo, ...currentArray])
    setToDo("")
  }

  return (
  <div>
    <h1> My Todos ({toDos.length})</h1>
    <form onSubmit={onSubmit}>
      <input 
        value={toDo} 
        onChange={onChange} 
        type="text" 
        placeholder="Wirte your to do.." 
      />
      <button>Add to do</button>
    </form>
    <hr />
    <ul>
    {toDos.map((item,index)=> (
      // key는 꼭 넣어야한다. 인식의 문제
      <li key={index}>{item}</li> 
    ))}
    </ul>
  </div>
  )
}

export default App