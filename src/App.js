import React from "react";
import { Route } from "react-router-dom";

import PostListPage from "./pages/PostListPage";

import "./App.css";

import PostPage from "./pages/PostPage";
import { Helmet } from "react-helmet-async";
function App() {
  return (
    <>
      <Route
        component={PostListPage}
        path={["/postlist/@:username", "/postlist"]}
      />
      <Route component={PostPage} path="/@:username/:postId" />
    </>
  );
}

export default App;
