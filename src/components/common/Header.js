import React, { useState } from "react";
import { Link, withRouter } from "react-router-dom";
import styled from "styled-components";
import Slide from "react-reveal/Slide";
import "./Header.css";
import menuIcon from "../../img/logo.png";

const LinkTo = styled(Link)`
  text-decoration: none;
  color: black;
  font-size: 15px;
  &:hover {
    color: #e8c74d;
  }
`;

const LogoImg = styled.img`
  height: 3rem;
`;

const Header = () => {
  const [menuToggle, setMenuToggle] = useState(false);

  const CkMenuToggle = () => {
    if (menuToggle) {
      setMenuToggle(!menuToggle);
      setTimeout(() => {
        document.getElementById("toggleMenus").style.display = "none";
      }, 720);
    } else {
      document.getElementById("toggleMenus").style.display = "block";
      setMenuToggle(!menuToggle);
    }
  };

  return (
    <>
      <div className="header">
        <div className="navBar_toggleBtn">
          <img
            className="menu_icon_img"
            alt="메뉴 드롭 아이콘"
            onClick={CkMenuToggle}
          />
        </div>
        <div>
          <Link to="/">
            <LogoImg src={menuIcon} />
          </Link>
        </div>
        <ul className="navBar_menus">
          <li className="navBar_menus_menu">
            <LinkTo to="/swing">SWING</LinkTo>
          </li>
          <li className="navBar_menus_menu">
            <LinkTo to="/board">게시판</LinkTo>
          </li>
        </ul>
      </div>
      <Slide top when={menuToggle}>
        <ul id="toggleMenus">
          <li className="navBar_menus_menu">
            <LinkTo to="/swing">SWING</LinkTo>
          </li>
          <li className="navBar_menus_menu">
            <LinkTo to="/board">게시판</LinkTo>
          </li>
        </ul>
      </Slide>
    </>
  );
};

export default Header;
