import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Responsive from './Responsive';
import styled from 'styled-components';
import { Link } from 'react-router-dom';
import palette from '../../lib/style/palette';
import './MainAbout.css';
import NavigateNextIcon from '@material-ui/icons/NavigateNext';


const Wrapper = styled(Responsive)`
    display: inline-flex;
    align-items: center;
    width: 100%;
    z-index: 100;
    justify-content: space-between; /* 자식 엘리먼트 사이에 여백을 최대로 설정 */
    @media only screen and (max-width: 700px) {
        display: inline-block;
    }
`;
const InDiv = styled(Responsive)`
    margin-top: 3px;
`;

const LinkTo = styled(Link)`
    &:hover{
        text-decoration: none;
    }
`;
const useStyles = makeStyles({
  root: {
    maxWidth: '370px', 
    height: '240px',
    margin: 'auto',
    boxShadow: '5px 5px 5px 3px #616161',
    marginBottom : '15px',
  },
  bullet: {
    display: 'inline-block',
    margin: '0 5px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 15,
    marginBottom : '10px',
  },
  pos: {
    marginBottom: 12,
  },
});

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


export default function MainCard() {
  const classes = useStyles();
  return (
    <>
    <About>
      <h2>TUTORIAL</h2>
    </About>
    <Wrapper>
    <InDiv>
    <Card className={classes.root}>
      <CardContent>
        <Typography className={classes.title} color="textSecondary" gutterBottom>
          STEP 1
        </Typography>
        <Typography variant="h5" component="h2">
          오늘의 스윙
        </Typography>
        <Typography variant="body2" component="p">
          <br/>
          시작 버튼을 누르고 골프스윙을 해보세요.<br/>
          스윙 자세를 인식하여 완료 후 분석을 해줍니다.           
        </Typography>
      </CardContent>
      <CardActions>
        <LinkTo to="/todaysw">
        <Button size="large" startIcon={<NavigateNextIcon />} style={{fontWeight:'bold'}}>지금 시작하기</Button>
        </LinkTo>
      </CardActions>
      </Card>
        </InDiv>
        <InDiv>
      <Card className={classes.root}>
      <CardContent>
        <Typography className={classes.title} color="textSecondary" gutterBottom>
          STEP 2
        </Typography>
        <Typography variant="h5" component="h2">
          게시판
        </Typography>
        <Typography variant="body2" component="p">
          <br/>
          골프장 정보, 스윙 리뷰, 골프용품 리뷰 등 다양한 이야기를 나누어 보세요.<br/>
          <br/>
        </Typography>
      </CardContent>
      <CardActions>
        <LinkTo to="/postlist">
        <Button size="large" startIcon={<NavigateNextIcon />}  style={{fontWeight:'bold'}}>지금 확인하기</Button>
        </LinkTo>
      </CardActions>
    </Card>
    </InDiv>
    </Wrapper>
    </>
  );
}