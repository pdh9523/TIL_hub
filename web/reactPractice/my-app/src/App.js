import Button from "./Button.js"
import styles from "./App.module.css"
import {useState} from "react"
function App() {
  const [value, setValue] = useState(0)
  const onClick = () => setValue((prev) => prev+1)

  return (  
    <div>
      <h1 className={styles.Title}> welcome Back! {value} </h1>
      <button onClick={onClick}>click Me</button>
    </div>
  );
}


export default App;
