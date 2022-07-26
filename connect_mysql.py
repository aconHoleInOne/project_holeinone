#python mysql 연동

import pymysql

def connect_mysql(host='127.0.0.1',user='HOLE_ADMIN',password='ADMIN1234',db="holeinone",charset='utf8'):
    #mysql connection 생성
    conn = pymysql.connect(host=host,user=user,password=password, db = db, charset=charset,autocommit=True,cursorclass =pymysql.cursors.DictCursor)
    # 
    #connection 으로 부터 cursor 생성
    cur = conn.cursor()
    
    print("mysql connect 성공");

    #cur sql 문 실행 하면 된다.
    return conn,cur

#사용 예시
# sql = "SELECT * FROM customers" # customers 테이블 전체를 불러옴
# cur.execute(sql)
# rows = cur.fetchall()
# con.close() # DB 연결 종료
# print(rows)