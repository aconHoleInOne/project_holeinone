import React, { useEffect, useState } from "react";
import styled from "styled-components";
import Fade from "react-reveal/Fade";
import { Link } from "react-router-dom";
import axios from "axios";
const Spacer = styled.div`
  height: 3.5rem;
`;

const Title = styled.div`
  padding-bottom: 50px;
  font-size: 50px;
  font-weight: bold;
  color: ${(props) => props.theme.accentColor};
  text-align: center;
`;

const Wrapper = styled.div`
  margin-top: 25px;
  text-align: center;
`;

const Hr = styled.hr`
  width: 250px;
  display: block;
`;

const PostWrap = styled.div`
  display: inline-block;
  width: 75%;
  text-align: left;
  margin-bottom: 45px;
  @media screen and (max-width: 768px) {
    width: 95%;
  }
`;

const PostLink = styled(Link)`
  display: block;
  text-decoration: none;
  color: black;
`;

const Table = styled.table`
  width: 100%;
  text-align: center;
  border-collapse: collapse;
  font-size: 13px;
  th {
    font-size: 15px;
  }
`;

const WhiteSpace = styled.div`
  height: 350px;
`;

const NoCont = styled.div`
  font-size: 15px;
  height: 400px;
  margin-top: 100px;
  text-align: center;
`;

const WriteButton = styled(Link)`
  width: 70px;
  padding: 10px;
  background: green;
  float: right;
  text-align: center;
  text-decoration: none;
  color: black;
  margin-bottom: 10px;
  border-radius: 5px;
  font-size: 13px;
  &:hover {
    background: lightgreen;
  }
`;

function Post() {
  const [coins, setCoins] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get("https://api.coinpaprika.com/v1/coins").then((results) => {
      let copy = [...coins, ...results.data];
      setCoins(copy.slice(0, 10));
    });
  });

  // useEffect(() => {
  //   (async () => {
  //     const rs = await fetch("https://api.coinpaprika.com/v1/coins");
  //     const json = await rs.json();
  //     setCoins(json.slice(0, 10));
  //     setLoading(false);
  //   })();
  // }, []);
  return (
    <>
      <Spacer />
      <Title>
        <Fade delay={400}>BOARD</Fade>
      </Title>
      <Fade delay={500}>
        <Wrapper>
          <PostWrap>
            <Table>
              <thead>
                <tr style={{ borderBottom: "1px solid gray" }}>
                  <th style={{ width: "15%", padding: "20px" }}>번호</th>
                  <th style={{ width: "70%" }}>제목</th>
                  <th style={{ width: "15%" }}>작성일</th>
                </tr>
              </thead>
              <tbody key={coins.name}>
                {coins.map((post, index) => (
                  <tr style={{ borderBottom: "1px solid lightgray" }}>
                    <td style={{ padding: "20px" }}>{coins.length - index}</td>
                    <td>
                      <PostLink
                        to={{ pathname: `/board/${post.id}` }}
                        state={post.name}
                      >
                        {post.id}
                      </PostLink>
                    </td>
                    <td>{}</td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </PostWrap>
        </Wrapper>
      </Fade>
    </>
  );
}

export default Post;
