import styles from "./App.module.css"
import {useState, useEffect} from "react"

function App() {
  const [counter, setCounter] = useState(0)
  const [keyword, setKeyword] = useState("")
  const onClick = () => setCounter((prev) => prev+1)
  const onChange = (event) => setKeyword(event.target.value)

  const getTitle = () => {
    console.log("i run only once")
  }
  useEffect(getTitle, [])
  // 한번만 실행되었으면 하는 경우 useEffect의 두번째 매개변수에 빈 리스트를 넣으면 된다.  => 지켜볼 대상이 없어서 빈 리스트라는 뜻
  useEffect(() => {
    console.log("I run only once")
  }, [])
  // 키워드가 변경되었을떄만 실행되었으면 하는 경우 리스트 안에 키워드를 넣으면 된다.
  useEffect(() => {
    console.log("I run when 'keyword' changes")
  }, [keyword])

  useEffect(() => {
    console.log("I run when 'counter' changes'")
  }, [counter])
  // 두 개 이상의 변수가 변경되었을 떄 실행되었으면 하는 경우 리스트 안에 다 집어넣으면 된다. 
  useEffect(() =>{ 
    console.log("I run when 'counter' or 'keyword' changes")
  }, [counter, keyword])
  return (  
    <div>
      <input 
        onChange={onChange}
        value={keyword}
        type="text" 
        placeholder="Search here..." />
      <h1 
        className={styles.Title}> 
        {counter} 
      </h1>
      <button onClick={onClick}>click Me</button>
    </div>
  );
}


export default App;
