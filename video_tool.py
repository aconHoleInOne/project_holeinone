from datetime import date
from typing import Final
import pymongo
# from pymongo import MongoClient
import gridfs
import datetime
import cv2
from connect_mongo import connect_mongo_golfDB
from PIL import Image


class video_tool:
    
    def __init__(self, database, user_id):
        self.database = database;
        self.user_id = user_id;
        self.upload_date = '';
        self.fs = gridfs.GridFS(self.database)

    def upload(self,video_path,upload_date=datetime.datetime.now()):
        self.upload_date = upload_date;
        video_data = open(video_path,"rb")
        fileName = f"{self.user_id}_{self.upload_date.year}{self.upload_date.month}{self.upload_date.day}_swing";
        self.fs.put(video_data,fileName=fileName,user_id=self.user_id, date=self.upload_date)


    def download(self):
        #최근에 다운로드 한것을 다운 받는다
        data = self.database.fs.files.find_one({"user_id":self.user_id,"date":self.upload_date})
        myid = data['_id']
        videoData = self.fs.get(myid)
        return videoData;
    

    def upload_image(self,image_data,image_name):
        try :
            image_data_s = open(image_data,"rb")
            self.fs.put(image_data_s,image_name=image_name, file_type="image", user_id=self.user_id,date = self.upload_date)
            return
        except Exception as e:
            print('몽고 디비에 이미지 저장 하다  에러 발생',e);
            return

# data = golf_db.fs.files.find_one({"user_id":user_id})
# print(data)
# myid = data['_id']

# outputdata = fs.get(myid).read()
# # output = open("mongodb_video.mp4","wb")
# # output.write(outputdata)
# # output.close()
# # print("download complete")



