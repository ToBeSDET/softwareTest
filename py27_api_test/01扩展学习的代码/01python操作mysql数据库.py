"""
============================
Author:柠檬班-木森
Time:2020/3/26   20:09
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
主机：120.78.128.25
port：3306
用户：future
密码：123456



"""

import pymysql

# 第一步：连接到数据库
conn = pymysql.connect(host="120.78.128.25",
                       port=3306,
                       user="future",
                       password="123456",
                       charset="utf8",
                       cursorclass = pymysql.cursors.DictCursor
                       )

# 第二步：创建一个游标对象
cur = conn.cursor()

sql = "SELECT * FROM futureloan.member LIMIT 10"

# 第三步：执行sql语句
res = cur.execute(sql)
print(res)

# 第四步：获取查询到的结果
# fetchone:获取查询到的一条数据
data = cur.fetchone()
print(data)

# data1 = cur.fetchone()
# print(data1)

# fetchall:获取查询到的所有数据
# datas = cur.fetchall()
# print(datas)