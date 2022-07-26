from connect_mysql import connect_mysql
from connect_mongo import connect_mongo_golfDB
import video_tool
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import feature_column
from sklearn.model_selection import train_test_split
import gridfs
import cv2
import io
import operator
from PIL import Image
import matplotlib.pyplot as plt
import math
import mediapipe as mp
#타이거
#내 영상
#wood vs 내 비교 해서 피드백 mysql




user_id = "bbb";  #rest api 로 받아온 아이디로 
#########################
###안되면 api 불러오기###
########################


# 게시판, 로그인 ,회원가입 키용님이랑 컨텍해서 서로 연동하기
conn,cur = connect_mysql();
sql =f"select * from img_landmark where member_id = \'{user_id}\' and upload_date = (select max(upload_date) from img_landmark where member_id=\'{user_id}\')";
cur.execute(sql);
rows = cur.fetchall();

# conn.close()


#mysql select 결과를 pandas 의 DataFrame 으로 타입 변환.
image_land_pd = pd.DataFrame(rows)

image_id_list=[];
def df_to_dataset(dataframe):
  dataframe = dataframe.copy()
  image_id_list.append(dataframe.pop('image_id'))
  dataframe.pop('upload_date')
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe)))
  return ds


golf_ds = df_to_dataset(image_land_pd)


#분류 모델 가져온다.
#colab 에서 만든 이미지 분류 모델이다. (0:address, 1:top, 2:finish) 3개로 분류되게 해주는 모델이다..
#정확도가 fit했을때는 높게 나왔는데 막상 실제 데이터를 넣어보면 엄청 높지 않은거 같다.
model = tf.keras.models.load_model("C:/Users/user/Desktop/acorn_model/my_model")


pred = model.predict(golf_ds.batch(32))

print(pd.DataFrame(pred).head())

address_dict = dict()
top_dict = dict()
finish_dict = dict()

cnt = 0
for p in pred:
    maxIndex = np.argmax(p)
    image_id = image_id_list[0][cnt];
    if maxIndex == 0 :
        address_dict[image_id] = p.max()
    elif maxIndex == 1:
        top_dict[image_id] = p.max();
    else:
        finish_dict[image_id] = p.max();
    cnt+=1


print("ADDRESS 로 분류된 이미지 개수 : ",len(address_dict))
print("top_swing 으로 분류된 이미지 개수 : ",len(top_dict))
print("finish 로 분류된 이미지 개수 : ",len(finish_dict))
print("--------------------------------------------------------------\n");

#분류된 이미지 중에서도 가장 정확도가 높은 이미지 1개씩 추출한다.

max_address_dict = max(address_dict.items(), key=operator.itemgetter(1))[0]
max_top_dict = max(top_dict.items(), key=operator.itemgetter(1))[0]
max_finish_dict = max(finish_dict.items(), key=operator.itemgetter(1))[0]

print("addr 정확도 수치 가장 높은 사진 : ",max_address_dict) 
print("top_swing 정확도 수치 가장 높은 사진 : ",max_top_dict)
print("finish 정확도 수치 가장 높은 사진 : ",max_finish_dict)
print("--------------------------------------------------------------\n");

#몽고 디비에서 이미지 저장한거 불러 온다.

id = "HOLE_ADMIN"
pwd = "ADMIN1234"
#mongo DB 연결
golf_db = connect_mongo_golfDB(id,pwd);
fs = gridfs.GridFS(golf_db)



#몽고 디비(golf_db) 에 저장되어 있는 이미지 파일 중 address 수치가 가장 높은 이미지를 가져오는 것이다.
addr_img_data = golf_db.fs.files.find_one({"user_id":user_id, "file_type":"image","image_name":max_address_dict})
top_img_data = golf_db.fs.files.find_one({"user_id":user_id, "file_type":"image","image_name":max_top_dict})
finish_img_data = golf_db.fs.files.find_one({"user_id":user_id, "file_type":"image","image_name":max_finish_dict})



#---------------------몽고디비로 받아온 이미지 시각화 하는 방법------------------------------------------#
addr_img_id = addr_img_data['_id'];
addr_img = fs.get(addr_img_id).read();
top_img_id = top_img_data['_id'];
top_img = fs.get(top_img_id).read();
finish_img_id = finish_img_data['_id'];
finish_img = fs.get(finish_img_id).read();
#받아온 이미지를 저장 파일로 저장하고
#저장한 이미지 파일을 읽어오는 느낌으로 해야하는거 같다
f = open(f"result/address_{user_id}.jpg", "wb")
f.write(addr_img)
f = open(f"result/top_{user_id}.jpg", "wb")
f.write(top_img)
f = open(f"result/finish_{user_id}.jpg", "wb")
f.write(finish_img)
# # cv2.imshow("tlqkf",addr_img);
#------------------------------------------------------------------------------------------------------#



def calculateAngle(landmark1, landmark2, landmark3):
  x1=0
  y1=0
  x2 =0
  y2=0
  x3=0
  y3=0
  if type(landmark1) == dict:
    x1 = landmark1['x']
    y1 = landmark1['y']
    x2 = landmark2['x']
    y2 = landmark2['y']
    x3 = landmark3['x']
    y3 = landmark3['y'] 
  else:
    x1 = landmark1.x
    y1 = landmark1.y
    x2 = landmark2.x
    y2 = landmark2.y
    x3 = landmark3.x
    y3 = landmark3.y


  angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))

  if angle < 0:
    angle += 360
  return angle



#포즈 감지 모델 초기화작업
mp_pose = mp.solutions.pose 
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)
mp_drawing = mp.solutions.drawing_utils


#타이거 우즈 어드레스 자세 각도.
tiger_addr_img = cv2.imread('tiger_address.png')
tiger_addr_results = pose.process(cv2.cvtColor(tiger_addr_img, cv2.COLOR_BGR2RGB))

#타이거 우즈 탑 스윙 자세 각도.
tiger_top_img = cv2.imread('tiger_top_swing.png')
tiger_top_results = pose.process(cv2.cvtColor(tiger_top_img, cv2.COLOR_BGR2RGB))

#타이거 우즈 피니시 자세 각도.
tiger_finish_img = cv2.imread('tiger_finish.png')
tiger_finish_results = pose.process(cv2.cvtColor(tiger_finish_img, cv2.COLOR_BGR2RGB))

tiger_angles = dict()
#dhalkfd
tiger_angles['address'] = {'waist':calculateAngle(tiger_addr_results.pose_landmarks.landmark[12], #r_shoulder_x,r_shoulder_y
                                                 tiger_addr_results.pose_landmarks.landmark[24], #r_hip_x, r_hip_y
                                                 tiger_addr_results.pose_landmarks.landmark[26]), #r_knee_x, r_knee_y

                          'knee':calculateAngle(tiger_addr_results.pose_landmarks.landmark[24],
                                                tiger_addr_results.pose_landmarks.landmark[26], 
                                                tiger_addr_results.pose_landmarks.landmark[28]), #r_ankle_x, r_ankle_y

                          'shoulder':calculateAngle(tiger_addr_results.pose_landmarks.landmark[14], #r_elbow_x, #r_elbow_y
                                                    tiger_addr_results.pose_landmarks.landmark[12],
                                                    tiger_addr_results.pose_landmarks.landmark[24])}

tiger_angles['top'] = {'waist':calculateAngle(tiger_top_results.pose_landmarks.landmark[11], #l_shoulder_x, #l_shoulder_y
                                              tiger_top_results.pose_landmarks.landmark[24], #r_hip_x, r_hip_y
                                              tiger_top_results.pose_landmarks.landmark[26]), #r_knee_x, r_knee_y

                        'right_elbow' : calculateAngle(tiger_top_results.pose_landmarks.landmark[16], #r_wrist_x,r_wrist_y
                                                       tiger_top_results.pose_landmarks.landmark[14], #r_elbow_x,r_elbow_y
                                                       tiger_top_results.pose_landmarks.landmark[12]), #r_shoulder_x, r_shoulder_y

                        'hands_angle' : calculateAngle(tiger_top_results.pose_landmarks.landmark[13], #l_elbow_x, l_elbow_y
                                                       tiger_top_results.pose_landmarks.landmark[15], #l_wrist_x, l_wrist_y
                                                       tiger_top_results.pose_landmarks.landmark[14])}

tiger_angles['finish'] = {'waist':calculateAngle(tiger_top_results.pose_landmarks.landmark[25], #l_knee_x, #l_knee_y
                                              tiger_top_results.pose_landmarks.landmark[23], #l_hip_x, l_hip_y
                                              tiger_top_results.pose_landmarks.landmark[12]),#r_shoulder_x,r_shoulder_y

                        'left_elbow' : calculateAngle(tiger_top_results.pose_landmarks.landmark[15], #l_wrist_x, l_wrist_y
                                                       tiger_top_results.pose_landmarks.landmark[13], #l_elbow_x, l_elbow_y
                                                       tiger_top_results.pose_landmarks.landmark[11])}#l_shoulder_x, #l_shoulder_y
print("tiger_angels : ", tiger_angles)                                


#유사도 가장 높은 address 사진 의 각도
max_address_sql = f"""
select r_shoulder_x,r_shoulder_y,r_hip_x, r_hip_y,r_knee_x, r_knee_y,r_ankle_x, r_ankle_y,r_elbow_x,r_elbow_y
from img_landmark 
where image_id = \'{max_address_dict}\'
""";
cur.execute(max_address_sql);
rows = cur.fetchall();

#address 자세에 필요한 각도만 추출해서 dataframe 으로 만들었다.
max_address_angles_data= pd.DataFrame(rows);


#유사도 가장 높은 top 사진 의 각도
max_top_sql = f"""
select l_shoulder_x,l_shoulder_y,r_hip_x, r_hip_y,r_knee_x, r_knee_y,r_wrist_x, r_wrist_y,r_elbow_x,r_elbow_y,r_shoulder_x,r_shoulder_y,l_elbow_x,l_elbow_y,l_wrist_x,l_wrist_y
from img_landmark 
where image_id = \'{max_top_dict}\'
""";

cur.execute(max_top_sql);
rows = cur.fetchall();

#address 자세에 필요한 각도만 추출해서 dataframe 으로 만들었다.
max_top_angles_data= pd.DataFrame(rows);


#유사도 가장 높은 finish 사진 의 각도
max_finish_sql = f"""
select l_knee_x, l_knee_y,l_hip_x, l_hip_y,r_shoulder_x,r_shoulder_y,l_wrist_x, l_wrist_y,l_elbow_x, l_elbow_y,l_shoulder_x,l_shoulder_y
from img_landmark
where image_id = \'{max_finish_dict}\'
""";

cur.execute(max_finish_sql);
rows = cur.fetchall();

#address 자세에 필요한 각도만 추출해서 dataframe 으로 만들었다.
max_finish_angles_data= pd.DataFrame(rows);



#사용자 스윙 각도 구하기
# addres : 허리, 무릎, 어깨 각도를 구해서 저장한다.
# top : 허리 오른쪽 어깨, 두 어깨의 각도
# finish : 허리, 왼쪽 어깨
#를 구해서 user_angles 라는 집합에 저장한다.
user_angles = dict();
user_angles['address'] = {'waist' : calculateAngle({'x': max_address_angles_data['r_shoulder_x'].values[0],'y': max_address_angles_data['r_shoulder_y'].values[0]},
                                    {'x':max_address_angles_data['r_hip_x'].values[0],'y':max_address_angles_data['r_hip_y'].values[0]},
                                    {'x':max_address_angles_data['r_knee_x'].values[0],'y':max_address_angles_data['r_knee_y'].values[0]}),
                                    
                          'knee' : calculateAngle({'x':max_address_angles_data['r_hip_x'].values[0],'y':max_address_angles_data['r_hip_y'].values[0]},
                                    {'x':max_address_angles_data['r_knee_x'].values[0],'y':max_address_angles_data['r_knee_y'].values[0]},
                                    {'x':max_address_angles_data['r_ankle_x'].values[0],'y':max_address_angles_data['r_ankle_y'].values[0]}),

                          'shoulder' : calculateAngle({'x':max_address_angles_data['r_elbow_x'].values[0],'y':max_address_angles_data['r_elbow_y'].values[0]},
                                    {'x':max_address_angles_data['r_shoulder_x'].values[0],'y':max_address_angles_data['r_shoulder_y'].values[0]},
                                    {'x':max_address_angles_data['r_hip_x'].values[0],'y':max_address_angles_data['r_hip_y'].values[0]})}


user_angles['top'] = {'waist' : calculateAngle({'x': max_top_angles_data['l_shoulder_x'].values[0],'y': max_top_angles_data['l_shoulder_y'].values[0]},
                                    {'x':max_top_angles_data['r_hip_x'].values[0],'y':max_top_angles_data['r_hip_y'].values[0]},
                                    {'x':max_top_angles_data['r_knee_x'].values[0],'y':max_top_angles_data['r_knee_y'].values[0]}),
                                    
                          'right_elbow' : calculateAngle({'x':max_top_angles_data['r_wrist_x'].values[0],'y':max_top_angles_data['r_wrist_y'].values[0]},
                                    {'x':max_top_angles_data['r_elbow_x'].values[0],'y':max_top_angles_data['r_elbow_y'].values[0]},
                                    {'x':max_top_angles_data['r_shoulder_x'].values[0],'y':max_top_angles_data['r_shoulder_y'].values[0]}),

                          'hands_angle' : calculateAngle({'x':max_top_angles_data['l_elbow_x'].values[0],'y':max_top_angles_data['l_elbow_y'].values[0]},
                                    {'x':max_top_angles_data['l_wrist_x'].values[0],'y':max_top_angles_data['l_wrist_y'].values[0]},
                                    {'x':max_top_angles_data['r_elbow_x'].values[0],'y':max_top_angles_data['r_elbow_y'].values[0]})}


user_angles['finish'] = {'waist' : calculateAngle({'x': max_finish_angles_data['l_knee_x'].values[0],'y': max_finish_angles_data['l_knee_y'].values[0]},
                                    {'x':max_finish_angles_data['l_hip_x'].values[0],'y':max_finish_angles_data['l_hip_y'].values[0]},
                                    {'x':max_finish_angles_data['r_shoulder_x'].values[0],'y':max_finish_angles_data['r_shoulder_y'].values[0]}),
                                    
                          'left_elbow' : calculateAngle({'x':max_finish_angles_data['l_wrist_x'].values[0],'y':max_finish_angles_data['l_wrist_y'].values[0]},
                                    {'x':max_finish_angles_data['l_elbow_x'].values[0],'y':max_finish_angles_data['l_elbow_y'].values[0]},
                                    {'x':max_finish_angles_data['l_shoulder_x'].values[0],'y':max_finish_angles_data['l_shoulder_y'].values[0]})}



#타이거 우주와  address, top, finish 각각의 비교할 각도들을 user 와 비교하여 +- 20 해당 범위에 대한 피드백을 작성한다.
addr_feedback = list()
top_feedback  = list()
finish_feedback = list()

for keys in user_angles:
  
  if keys == 'address':
    addr_waist = tiger_angles['address']['waist'] - user_angles['address']['waist']
    addr_knee = tiger_angles['address']['knee'] - user_angles['address']['knee']
    addr_shoulder = tiger_angles['address']['shoulder'] - user_angles['address']['shoulder']

    if addr_waist > 20:
      addr_feedback.append("어드레스 자세에서 허리를 좀 펴주세요.")
    elif addr_waist < -20:
      addr_feedback.append("어드레스 자세에서 허리를 더욱 굽혀주세요.")
    else :
      addr_feedback.append("좋은 어드레스 자세입니다.")

    if addr_knee > 20:
      addr_feedback.append("어드레스 자세에서 무릎를 좀 펴주세요.")
    elif addr_knee < -20:
      addr_feedback.append("어드레스 자세에서 무릎을 더욱 굽혀주세요.")
    else :
      addr_feedback.append("좋은 어드레스 무릎 자세입니다.")

    if addr_shoulder > 20:
      addr_feedback.append("어드레스 자세에서 어깨에 좀 떨어.")
    elif addr_shoulder < -20:
      addr_feedback.append("어드레스 자세에서 팔을 어깨에 더 붙혀.")
    else :
      addr_feedback.append("좋은 어드레스 어깨 자세입니다.")
  elif keys == 'top':
    top_waist = tiger_angles['top']['waist'] - user_angles['top']['waist']
    top_right_elbow = tiger_angles['top']['right_elbow'] - user_angles['top']['right_elbow']
    top_hands_angle = tiger_angles['top']['hands_angle'] - user_angles['top']['hands_angle']

    # 음수 가 오면 각도를 좀 줄여라
    # 양수가 나오면 각도를 더 키워라 
    if top_waist > 20:
      top_feedback.append("탑 스윙 자세에서 허리를 조금더 펴주세요.")
    elif top_waist < -20:
      top_feedback.append("탑 스윙 자세에서 허리를 조금더 굽혀주세요.")
    else:
      top_feedback.append("좋은 허리 각도입니다.")
    
    if top_right_elbow >20:
      top_feedback.append("오른쪽 팔꿈치를 조금 더 펴주세요.");
    elif top_right_elbow <-20:
      top_feedback.append("오른쪽 팔꿈치를 조금더 굽혀 주세요.")
    else:
      
      top_feedback.append("좋은 팔 각도 입니다.")
    
    if top_hands_angle > 20:
      top_feedback.append("팔을 좀더 떨어뜨려 주세요.")
    elif top_hands_angle < -20:
      top_feedback.append("팔을 좀더 붙혀 주세요.")
    else :
      top_feedback.append("좋은 팔 간격입니다.")
  else:
    finish_waist = tiger_angles['finish']['waist'] - user_angles['address']['waist']
    finish_left_elbow = tiger_angles['finish']['left_elbow'] - user_angles['finish']['left_elbow']

    if finish_waist > 20:
      finish_feedback.append("피니시 자세에서 허리를 좀 펴주세요.")
    elif finish_waist < -20:
      finish_feedback.append("피니시 자세에서 허리를 더욱 굽혀주세요.")
    else :
      finish_feedback.append("좋은 허리각도 입니다.")

    if finish_left_elbow > 20:
      finish_feedback.append("왼쪽 팔꿈치를 좀 펴주세요.")
    elif finish_left_elbow < -20:
      finish_feedback.append("왼쪽 팔꿈치을 더욱 굽혀주세요.")
    else :
      finish_feedback.append("좋은 왼쪽 팔꿈치 자세입니다.")




#mysql 에 user_id, date, addr_feedback, top_feedback, finish_feedback....
# user_id 가 스윙 이미지3개( address,top,finish 중에서 가장 정확도 수치가 높은 이미지) , 피드백,

# conn,cur = connect_mysql();
sql = """
insert into  swing_result(member_id,address_img,top_img,finish_img,address_feedback,top_feedback,finish_feedback)
values(%s,%s,%s,%s,%s,%s,%s)
""";
val = (user_id,max_address_dict,max_top_dict,max_finish_dict,str(addr_feedback),str(top_feedback),str(finish_feedback))
try:
  cur.execute(sql,val);
except Exception as e:
  print("안녕 나 mysql 에러 : ",e)
conn.close()