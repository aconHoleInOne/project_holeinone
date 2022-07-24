import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';
import Responsive from './Responsive';
const NavBlock = styled.div`
  position: fixed;
  width: 100%;
  z-index:100;
  background: rgba(0,0,0,0.8);
`;

const Wrapper = styled(Responsive)`
    height: 3.5rem;
    display: flex;
    align-items: center;
    justify-content: space-evenly; /* 자식 엘리먼트 사이에 여백을 최대로 설정 */
`;

const Spacer = styled.div`
  height: 0.3rem;
`;

const LinkTo = styled(Link)`
    font-size: 0.9em;
    color: white;
    font-weight: bold;
    &:hover{
        text-decoration: none;
        color: #afafaf;
    }
`;
const Navbar = () => {
    return (
        <>
        <NavBlock>
            <Wrapper>
                <LinkTo to="/todaysw" className="logo">
                    오늘의 스윙
                </LinkTo>
                <LinkTo to="/postlist" className="logo">
                    게시판
                </LinkTo>
            </Wrapper>
        </NavBlock>
        <Spacer />
        </>
    );
};

export default Navbar;
