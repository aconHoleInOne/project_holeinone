import React from "react";
import { Route} from "react-router-dom";
import "./App.css";
import { Helmet } from "react-helmet-async";
import PostListPage from "./pages/PostListPage";
import PostPage from "./pages/PostPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import MainPage from "./pages/MainPage";
function App() {
  return (
    <>
      <Helmet>
        <title>HOLEINONE</title>
      </Helmet>
      <Route component={PostListPage} path={["/postlist/@:username", "/postlist"]} />
      <Route component={PostPage} path="/@:username/:postId" />
      <Route component={LoginPage} path="/login" />
      <Route component={RegisterPage} path="/register" />
      <Route component={MainPage} path="/main" />
    
    </>
  );
}

export default App;
