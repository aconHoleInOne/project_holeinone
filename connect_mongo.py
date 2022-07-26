from pymongo import MongoClient

#id = "HOLE_ADMIN"
#pwd = "ADMIN1234"
#인증 모드로 접속하는 함수!
def connect_mongo_golfDB(id, pwd):
   conn = MongoClient(f"mongodb://{id}:{pwd}@localhost");
   golf_db = conn["golf_db"]
   return golf_db;


# golf_videos = golf_db["golf_videos"] #db에서 사용할 table(collection)
# golf_images = golf_db["golf_images"] #db에서 사용할 table(collection)







