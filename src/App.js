import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Route, Routes } from "react-router-dom";
import Main from "../src/pages/Main.js";
function App() {
  return (
    <Routes>
      <Route element={<Main />} path="/" />
    </Routes>
  );
}

export default App;
