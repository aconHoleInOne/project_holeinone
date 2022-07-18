import React, { useState, useEffect } from "react";
import Header from "../common/Header";
import Footer from "../common/Footer";
import styled from "styled-components";
import Fade from "react-reveal/Fade";
import { Link, withRouter, useParams } from "react-router-dom";
import axios from "axios";

const Spacer = styled.div`
  height: 3.5rem;
`;

const Wrapper = styled.div`
  margin-top: 80px;
  margin-bottom: 45px;
  text-align: center;
`;

const PostWrap = styled.div`
  display: inline-block;
  width: 80%;
  text-align: left;
`;

const Head = styled.div`
  position: relative;
`;

const Title = styled.div`
  font-size: 23px;
  font-weight: bold;
  margin-bottom: 10px;
  padding-left: 50px;
`;

const Pre = styled.pre`
  font-size: 13px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  letter-spacing: 1px;
  padding-left: 50px;
  padding-right: 50px;
  line-height: 1.4;
  height: 500px;
  overflow: auto;
`;

const Date = styled.div`
  display: inline-block;
  font-size: 12px;
  padding-left: 50px;
`;

const Hr = styled.hr`
  color: lightgray;
  border-width: 1px 0px 0px 0px;
  opacity: 0.5;
  margin-bottom: 70px;
`;

const ButtonWrap = styled.div`
  position: absolute;
  bottom: 0;
  right: 0;
`;

const Button = styled.div`
  display: inline-block;
  width: 50px;
  padding: 7px;
  margin-left: 5px;
  background: gray;
  cursor: pointer;
  font-size: 13px;
  text-decoration: none;
  color: black;
  text-align: center;
  border-radius: 5px;
  &:hover {
    background: lightgray;
  }
`;

const ButtonTo = styled(Link)`
  display: inline-block;
  width: 50px;
  padding: 7px;
  margin-left: 5px;
  background: gray;
  cursor: pointer;
  font-size: 13px;
  text-decoration: none;
  color: black;
  text-align: center;
  border-radius: 5px;
  &:hover {
    background: lightgray;
  }
`;

function PostContent({ match, history }) {
  const [post, setPost] = useState([]);
  const { coinId } = useParams();

  return (
    <>
      <Header />
      <Spacer />
      <Fade delay={500}>
        <Wrapper>
          <PostWrap>
            <Head>
              <Title>임의의 제목</Title>
              <Date>작성일 : {}</Date>
              <ButtonWrap>
                <ButtonTo to="/board">목록</ButtonTo>
              </ButtonWrap>
            </Head>
            <Hr />

            <Pre>어쩌구 저쩌구 ㅇㅇ</Pre>
          </PostWrap>
        </Wrapper>
      </Fade>
      <Footer />
    </>
  );
}

export default PostContent;
