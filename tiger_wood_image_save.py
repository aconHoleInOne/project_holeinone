#tiger woods 의 사진을 몽고 디비에 저장.

from connect_mongo import connect_mongo_golfDB
from video_tool import video_tool
import cv2

#mongo DB id,pwd 사용자 인증 모드로 들어가야 crud 가 잘된다.
id = "HOLE_ADMIN"
pwd = "ADMIN1234"

#mongo DB 연결
golf_db = connect_mongo_golfDB(id,pwd);

#HOLE_ADMIN 으로 등록한다. (비교용으로 사용할거라서)
user_id = "HOLE_ADMIN"

#동영상 저장& 이미지 저장할라고 만든 클래스;
#download 는 만들었는데 사용 안할거같음; (대충 만들어서 ㅈ망했다는 소리)
vt = video_tool(golf_db,user_id);
#경로명은 바꿔서 해야한다.
# tiger_addr = "C:/Users/user/Desktop/acorn_model/tiger_address.PNG"
# tiger_top = "C:/Users/user/Desktop/acorn_model/tiger_top_swing.PNG"
# tiger_finish ="C:/Users/user/Desktop/acorn_model/tiger_finish.PNG"
tiger_pose = ["tiger_addr","tiger_top","tiger_finish"]
tiger_img_path_list = ["tiger_address.png",
                       "tiger_top_swing.PNG",
                       "tiger_finish.PNG"]

cnt = 0;
for img_path in tiger_img_path_list:
    image_name = tiger_pose[cnt];
    cnt+=1
    vt.upload_image(img_path,image_name);


