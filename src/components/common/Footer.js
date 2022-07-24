import React from "react";
import { Link } from 'react-router-dom';
import './Footer.css';

const Footer = () => {
  return (
    <div className="mt-5 pt-5 pb-5 footer">
    <div className="container">
      <div className="row">
        <div className="col-lg-5 col-xs-12 about-company">
          <h2 style={{fontStyle: 'oblique', fontWeight:'bold'}}>My AI Golf Trainer</h2>
          <p className="pr-3">당신만의 개인 트레이너가 되어드립니다!<br/>지금 바로 골프를 시작하고 당신의 자세를 분석해보세요!</p>
        </div>
        <div className="col-lg-3 col-xs-12 links">
          <h4 className="mt-lg-0 mt-sm-3"><i className="fa fa-link mr-3"></i>Quick Links</h4>
            <ul className="m-0 p-0">
              <li>- <Link to="/todaysw">오늘의 스윙</Link></li>
              <li>- <Link to="/postlist">게시판</Link></li>
            </ul><p></p>
        </div>
        <div className="col-lg-4 col-xs-12 location">
          <h4 className="mt-lg-0 mt-sm-4"><i className="fa fa-user-tie mr-3"></i> Contact Us!</h4>
          <p>서울특별시 마포구 양화로 122 LAB7빌딩 3층, 4층 에이콘아카데미 홍대</p>
          <p className="mb-0"><i className="fa fa-phone mr-3"></i>(02) 123-4567</p>
          <p className="mb-0"><i className="fa fa-envelope mr-3"></i>listener@gmail.com</p>
        </div>
      </div>
      <div className="row mt-5">
        <div className="col copyright">
            <h4 className="mt-lg-0 mt-sm-4 developer">‍<i class="fas fa-code"></i> Developers</h4>
            <p className="m-1 p-1">
                <span className="dev"><a href = "https://github.com/Minhyeok1998"><i className="fab fa-github-square mr-3"></i></a> 강민혁 </span>
                <span className="dev"><a href = "https://github.com/syp0812"><i className="fab fa-github-square mr-3"></i></a> 박소현 </span>
                <span className="dev"><a href = "https://github.com/QTSYQ"><i className="fab fa-github-square mr-3"></i></a> 유국토 </span>
                <span className="dev"><a href = "https://github.com/xxkidragon"><i className="fab fa-github-square mr-3"></i></a> 정기용 </span>
                <span className="dev"><a href = "https://github.com/ChoiMinSub"><i className="fab fa-github-square mr-3"></i></a> 최민섭 </span>
                <span className="dev"><a href = "https://github.com/zhyunp"><i className="fab fa-github-square mr-3"></i></a> 박제현 </span>
            </p>
          <p></p>
          <p>© 2021. All Rights Reserved.<br/> <a href="https://github.com/aconHoleInOne/project_holeinone" style={{color:'#afafaf'}}>project_holeinone</a></p>
        </div>
      </div>
    </div>
    </div>
  );
}

export default Footer;