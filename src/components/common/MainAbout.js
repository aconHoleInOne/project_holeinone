import React from 'react';
import styled from 'styled-components';
import Responsive from './Responsive';
import palette from '../../lib/style/palette';
import './MainAbout.css';

const About = styled(Responsive)`
    h2 {
      font-family: 'Poppins', sans-serif;
        padding : 15px;
        margin-bottom : 70px;
        font-size : 2.5rem;
        border-bottom : 2px solid ${palette.gray[5]};
    }
    p {
      margin-bottom : 5px;
      font-style : italic;
      font-size : 1.1rem;
    }
    span {
      font-size : 1.1rem;
      font-weight : bold;
    }
    text-align : center; 
`;

const Paragraph = styled.div`
    margin-top : 60px;
`;

const Spacer = styled.div`
  height: 10rem;
`;

const MainAbout = () => {
    return (
      <>
        <About className = "about">
            <h2>ABOUT</h2>
            <Paragraph>
              <p><span>HOLEINONE</span>는</p>
              <p>딥러닝을 기반으로 하여 골프 스윙 자세를 인식하고, 분석을 통해 자세를 교정해주는</p>
              <p>AI 골프스윙 동작 웹페이지입니다.</p>
            </Paragraph>
            <Paragraph>
              <p>나만의 트레이너인 홀인원과 함께 스윙연습을 하며 올바른 스윙자세를 만들어보세요.</p>
              <p></p>
            </Paragraph>
        </About>
        <Spacer />
      </>
    );
  };
  
  export default MainAbout;