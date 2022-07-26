from datetime import datetime
from distutils.command.upload import upload
import mediapipe as mp
from connect_mysql import connect_mysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2


mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3,model_complexity=2)
mp_drawing = mp.solutions.drawing_utils

#손가락 제외 할라고 튜플 만듬
extend_list = (20,18,22,21,17,19)
def skeleton_save_mysql(image_data, image_id,user_id, upload_date):
    #mysql connect 호출 사진에 스켈레톤 으로 찍힌 position 정보를 저장해야 한다.
    # db : holeinone table : img_landmark  에 저장한다
    mysql_connector, mysql_cur = connect_mysql();
    try:
        # print(f"skeleton_save_mysql upload_date : {upload_date}")
        #image 를 스켈레톤 입혔을때 position 결과
        results = pose.process(cv2.cvtColor(image_data,cv2.COLOR_BGR2RGB))
        r_shoulder_x=0;r_shoulder_y=0;r_shoulder_z=0;
        l_shoulder_x=0;l_shoulder_y=0;l_shoulder_z=0;
        r_elbow_x=0;r_elbow_y=0;r_elbow_z=0;
        l_elbow_x=0;l_elbow_y=0;l_elbow_z=0;
        r_wrist_x=0;r_wrist_y=0;r_wrist_z=0;
        l_wrist_x=0;l_wrist_y=0;l_wrist_z=0;
        r_hip_x=0;r_hip_y=0;r_hip_z=0;
        l_hip_x=0;l_hip_y=0;l_hip_z=0;
        r_knee_x=0;r_knee_y=0;r_knee_z=0;
        l_knee_x=0;l_knee_y=0;l_knee_z=0;
        r_ankle_x=0;r_ankle_y=0;r_ankle_z=0;
        l_ankle_x=0;l_ankle_y=0;l_ankle_z=0;
        r_heel_x=0;r_heel_y=0;r_heel_z=0;
        l_heel_x=0;l_heel_y=0;l_heel_z=0;
        r_foot_x=0;r_foot_y=0;r_foot_z=0;
        l_foot_x=0;l_foot_y=0;l_foot_z=0;
        if results.pose_landmarks:
            print(image_id," 등록 중 ...")
            for i in range(12,33,1):
                if i in extend_list:
                    continue;
                else:
                    name = mp_pose.PoseLandmark(i).name;
                    value_sets = results.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value];
                    if name =='RIGHT_SHOULDER':
                        r_shoulder_x = value_sets.x;
                        r_shoulder_y= value_sets.y;
                        r_shoulder_z = value_sets.z;
                    elif name == 'LEFT_SHOULDER':
                        l_shoulder_x = value_sets.x;
                        l_shoulder_y= value_sets.y;
                        l_shoulder_z = value_sets.z;
                    elif name == 'RIGHT_ELBOW':
                        r_elbow_x = value_sets.x;
                        r_elbow_y = value_sets.y;
                        r_elbow_z = value_sets.z;
                    elif name == 'LEFT_ELBOW':
                        l_elbow_x = value_sets.x;
                        l_elbow_y = value_sets.y;
                        l_elbow_z = value_sets.z;
                    elif name == 'RIGHT_WRIST':
                        r_wrist_x=value_sets.x;
                        r_wrist_x=value_sets.y;
                        r_wrist_x=value_sets.z;
                    elif name == 'LEFT_WRIST':
                        l_wrist_x=value_sets.x;
                        l_wrist_x=value_sets.y;
                        l_wrist_x=value_sets.z;
                    elif name == 'RIGHT_HIP':
                        r_hip_x = value_sets.x;
                        r_hip_y = value_sets.y;
                        r_hip_z = value_sets.z;
                    elif name == 'LEFT_HIP':
                        l_hip_x = value_sets.x;
                        l_hip_y = value_sets.y;
                        l_hip_z = value_sets.z;
                    elif name == 'RIGHT_KNEE':
                        r_knee_x = value_sets.x;
                        r_knee_y = value_sets.y;
                        r_knee_z = value_sets.z;
                    elif name == 'LEFT_KNEE':
                        l_knee_x = value_sets.x;
                        l_knee_y = value_sets.y;
                        l_knee_z = value_sets.z;
                    elif name == 'RIGHT_ANKLE':
                        r_ankle_x=value_sets.x;
                        r_ankle_y=value_sets.y;
                        r_ankle_z=value_sets.z;
                    elif name == 'LEFT_ANKLE':
                        l_ankle_x=value_sets.x;
                        l_ankle_y=value_sets.y;
                        l_ankle_z=value_sets.z;
                    elif name == 'RIGHT_HEEL':
                        r_heel_x=value_sets.x;
                        r_heel_y=value_sets.y;
                        r_heel_z=value_sets.z;
                    elif name == 'LEFT_HEEL':
                        l_heel_x=value_sets.x;
                        l_heel_y=value_sets.y;
                        l_heel_z=value_sets.z;
                    elif name == 'RIGHT_FOOT_INDEX':
                        r_foot_x=value_sets.x;
                        r_foot_y=value_sets.y;
                        r_foot_z=value_sets.z;
                    elif name == 'LEFT_FOOT_INDEX':
                        l_foot_x=value_sets.x;
                        l_foot_y=value_sets.y;
                        l_foot_z=value_sets.z; 
                
        # 17*3
        # INSERT INTO img_landmark(image_id,upload_date,member_id,r_shoulder_x,r_shoulder_y,r_shoulder_z,l_shoulder_x,l_shoulder_y,l_shoulder_z,r_elbow_x,r_elbow_y,r_elbow_z,l_elbow_x,l_elbow_y,l_elbow_z,r_wrist_x,r_wrist_y,r_wrist_z,l_wrist_x,l_wrist_y,l_wrist_z,r_hip_x,r_hip_y,r_hip_z,l_hip_x,l_hip_y,l_hip_z,r_knee_x,r_knee_y,r_knee_z,l_knee_x,l_knee_y,l_knee_z,r_ankle_x,r_ankle_y,r_ankle_z,l_ankle_x,l_ankle_y,l_ankle_z,r_heel_x,r_heel_y,r_heel_z,l_heel_x,l_heel_y,l_heel_z,r_foot_x,r_foot_y,r_foot_z,l_foot_x,l_foot_y,l_foot_z)
            if mysql_connector :
                sql = """insert into img_landmark(image_id,upload_date,member_id,r_shoulder_x,r_shoulder_y,r_shoulder_z,l_shoulder_x,l_shoulder_y,l_shoulder_z,
r_elbow_x,r_elbow_y,r_elbow_z,l_elbow_x,l_elbow_y,l_elbow_z,r_wrist_x,r_wrist_y,r_wrist_z,l_wrist_x,l_wrist_y,l_wrist_z,r_hip_x,r_hip_y,r_hip_z,
l_hip_x,l_hip_y,l_hip_z,r_knee_x,r_knee_y,r_knee_z,l_knee_x,l_knee_y,l_knee_z,r_ankle_x,r_ankle_y,r_ankle_z,l_ankle_x,l_ankle_y,l_ankle_z,r_heel_x,r_heel_y,r_heel_z,l_heel_x,
l_heel_y,l_heel_z,r_foot_x,r_foot_y,r_foot_z,l_foot_x,l_foot_y,l_foot_z)  values(
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s)"""

                
                val = (image_id,str(upload_date),user_id,r_shoulder_x,r_shoulder_y,r_shoulder_z,l_shoulder_x,l_shoulder_y,l_shoulder_z,r_elbow_x,r_elbow_y,r_elbow_z,l_elbow_x,l_elbow_y,l_elbow_z,r_wrist_x,r_wrist_y,r_wrist_z,l_wrist_x,l_wrist_y,l_wrist_z,r_hip_x,r_hip_y,r_hip_z,l_hip_x,l_hip_y,l_hip_z,r_knee_x,r_knee_y,r_knee_z,l_knee_x,l_knee_y,l_knee_z,r_ankle_x,r_ankle_y,r_ankle_z,l_ankle_x,l_ankle_y,l_ankle_z,r_heel_x,r_heel_y,r_heel_z,l_heel_x,l_heel_y,l_heel_z,r_foot_x,r_foot_y,r_foot_z,l_foot_x,l_foot_y,l_foot_z)

                # print(val)

                mysql_cur.execute(sql,val)
                print(f"{image_id}저장 완료")
    except Exception as e:
        print('mysql 스켈레톤 저장하다 에러 발생',e);
        return
    
