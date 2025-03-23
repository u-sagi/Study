import pymysql


# 连接数据库
db = pymysql.connect(user='root', password='1234', host='192.168.88.2', database='employees')
# 获取数据库(游标)
cursor = db.cursor()

# sql更新语句
sql_str = 'UPDATE employees SET gender="M" WHERE emp_no=10001'
# 执行sql语句
cursor.execute(sql_str)
# 额外执行commit()方法才能执行成功
db.commit()