import Footer from "../components/common/Footer.js";
import Header from "../components/common/Header.js";
import MainAbout from "../components/main/mainAbout.js";
import PhotoSlide from "../components/main/photoSlide.js";
function Main() {
  return (
    <div>
      <Header />
      <PhotoSlide />
      <MainAbout />
      <Footer />
    </div>
  );
}

export default Main;
