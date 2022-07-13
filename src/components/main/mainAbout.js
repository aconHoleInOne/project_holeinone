import React from "react";
import styled from "styled-components";
import Zoom from "react-reveal/Zoom";
import Fade from "react-reveal/Fade";

const Wrapper = styled.div`
  width: 100%;
  background: ${(props) => props.theme.bgColor};
  padding-top: 60px;
  padding-bottom: 60px;
  text-align: center;
`;

const Title = styled.div`
  padding-bottom: 50px;
  font-size: 50px;
  font-weight: bold;
  color: ${(props) => props.theme.accentColor};
`;

const DivWrap = styled.div`
  display: inline-block;
  position: relative;
  width: 380px;
  height: 380px;
  background: ${(props) => props.theme.boxColor};
  color: ${(props) => props.theme.textColor};
  margin: 10px;
  @media screen and (max-width: 768px) {
    width: 350px;
  }
`;

const Div = styled.div`
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  #title-top {
    padding-top: 60px;
    font-size: 15px;
    padding-bottom: 10px;
    letter-spacing: 1px;
  }
  #title-bottom {
    color: ${(props) => props.theme.textColor};
    font-size: 35px;
    font-weight: bold;
    padding-bottom: 50px;
  }
  #content {
    width: 380px;
    font-size: 18px;
    line-height: 30px;
  }
`;

const FadeWrap = styled.div`
  display: inline-block;
`;

function MainAbout() {
  return (
    <>
      <Wrapper>
        <Zoom>
          <Title>ABOUT</Title>
        </Zoom>
        <FadeWrap>
          <Fade delay={500} bottom>
            <DivWrap>
              <Div>
                <div id="title-top">어쩌구 저쩌구</div>
                <div id="title-bottom">이러쿵 저러쿵</div>
                <div id="content">
                  할말 적기
                  <br />
                  할말 적기
                  <br />
                  할말 적기
                  <br />
                  할말 적기
                </div>
              </Div>
            </DivWrap>
          </Fade>
        </FadeWrap>
        <FadeWrap>
          <Fade delay={1000} bottom>
            <DivWrap>
              <Div>
                <div id="title-top">어쩌구 저쩌구</div>
                <div id="title-bottom">이러쿵 저러쿵</div>
                <div id="content">
                  할말 적기
                  <br />
                  할말 적기
                  <br />
                  할말 적기
                  <br />
                  할말 적기
                </div>
              </Div>
            </DivWrap>
          </Fade>
        </FadeWrap>
        <FadeWrap>
          <Fade delay={1500} bottom>
            <DivWrap>
              <Div>
                <div id="title-top">어쩌구 저쩌구</div>
                <div id="title-bottom">이러쿵 저러쿵</div>
                <div id="content">
                  할말 적기
                  <br />
                  할말 적기
                  <br />
                  할말 적기
                  <br />
                  할말 적기
                </div>
              </Div>
            </DivWrap>
          </Fade>
        </FadeWrap>
      </Wrapper>
    </>
  );
}

export default MainAbout;
