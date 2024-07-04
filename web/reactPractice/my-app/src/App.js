import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom"
import Home from "./routes/Home"
import Detail from "./routes/Detail"
function App() {
  return (
  <Router>
    <Switch>
      // 상세 페이지
      <Route path="/movie/:id">
        <Detail />
      </Route>
      // 메인 페이지
      <Route path="/">
        <Home />
      </Route>
      

    </Switch>
  </Router>
  )
}
export default App