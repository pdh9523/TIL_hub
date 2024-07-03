import {useState, useEffect} from "react"

function Hello() {
  useEffect(function() {
    console.log("Hi :)")
    // cleanup function : useEffect가 return 하는 함수는 useEffect가 만든 component가 사라질 때 발생한다.
    return function() {
      console.log("Bye :(")
    }
  },[]) 
  return <h1> Hello</h1>;
}


function App() {
  const [showing, setShowing] = useState(false)
  const onClick = () => setShowing((prev)=> !prev)


  return (
    <div>
      {showing ? <Hello /> : null}
      <button onClick={onClick}>{showing? "Hide" : "Show"} </button>
    </div>
  )
}

export default App;