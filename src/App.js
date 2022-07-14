import "bootstrap/dist/css/bootstrap.min.css";
import { Route, Routes } from "react-router-dom";
import Main from "../src/pages/Main.js";
import Board from "./pages/Board";
function App() {
  return (
    <Routes>
      <Route element={<Main />} path="/" />
      <Route element={<Board />} path="/Board">
        {/* <Route path="/detail/:id"></Route> */}
      </Route>
      <Route path="*">없는 페이지</Route>
    </Routes>
  );
}

export default App;
