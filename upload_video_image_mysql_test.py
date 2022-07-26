from connect_mongo import connect_mongo_golfDB
from video_tool import video_tool
import cv2;
import mediapipe as mp
from connect_mysql import connect_mysql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from skeleton_save import skeleton_save_mysql 
from connect_mysql import connect_mysql
import os
import shutil
from PIL import Image
import random



#mongo DB id,pwd 사용자 인증 모드로 들어가야 crud 가 잘된다.
id = "HOLE_ADMIN"
pwd = "ADMIN1234"

#mongo DB 연결
golf_db = connect_mongo_golfDB(id,pwd);


#스윙친 user_id 이다. 구현할때는 user_id  받아와서 사용해야 한다.
user_id = "bbb"

#동영상 저장& 이미지 저장할라고 만든 클래스;
#download 는 만들었는데 사용 안할거같음; (대충 만들어서 ㅈ망했다는 소리)
vt = video_tool(golf_db,user_id);

video_path ="C:/Users/user/Desktop/acorn_model/1158.mp4"
vt.upload(video_path)

# video_data = vt.download()
cap = cv2.VideoCapture(video_path);
success = True
count = 0





#이미지 임시 저장 폴더 생성
image_folder_path = './image'
os.makedirs(image_folder_path, exist_ok=True)


while success:
    try:
        success,image = cap.read()
        randomNum = random.randrange(1,20000) #이미지 이름에 랜덤 숫자 붙히기
        image_name = f"{vt.user_id}_{vt.upload_date.year}{vt.upload_date.month}{vt.upload_date.day}_swingImage_{randomNum}_{count}.jpg"# 이거 이미지 수정
        image_save_location = f"{image_folder_path}/{image_name}"
        print("image_save_location : ", image_save_location)
        cv2.imwrite(image_save_location,image);
        count+=1;
        #mongo db 에 동영상을 이미지로 쪼개서 이미지 파일로 저장하는 함수이다.
        # cv2.imshow('',image);
        # vt.fs.put(tlqkf,image_name=image_name,file_type="image", user_id=vt.user_id,date = vt.upload_date)
        vt.upload_image(image_save_location,image_name);
        #image를 mediapipe 모델 사용 해서 skelton 을 입히고 각 관절 포지션을 야무지게 정리해서 mysql holeinone.img_landmark 에 저장하자.
        # 함수 호출
        skeleton_save_mysql(image,image_name,vt.user_id,vt.upload_date)
    except Exception as e:
        print(f"대충 이미지 보여주다 에러 생겼다는 소리 : {e.with_traceback}");
        break;
    if cv2.waitKey(50) == 27:
        break;

shutil.rmtree(image_folder_path)

#몽고 디비 데이터 저장 -> 01010이미지
#몽고디비에서 동영상을 슬라이스 가 best

cap.release()






        