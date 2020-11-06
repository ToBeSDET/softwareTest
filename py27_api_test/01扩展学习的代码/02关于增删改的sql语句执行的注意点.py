"""
============================
Author:柠檬班-木森
Time:2020/3/26   20:31
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
pymysql模块操作数据库：默认是开启了事务

所以在执行增删改的相关操作之后一定要提交事务才会生效
连接对象.commit()


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

# 假设下面是增删改的sql语句
sql = "SELECT * FROM futureloan.member LIMIT 10"

# 第三步：执行sql
cur.execute(sql)


# 第四步：提交事务
conn.commit()

