"""
============================
Author:柠檬班-木森
Time:2020/3/26   20:39
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
封装的需求：
    1、查询数据的方法
    2、增删改的方法
    3、init方法：建立连接


"""
import pymysql


class HandleMysql:

    def __init__(self):
        """初始化方法中，连接到数据库"""
        # 建立连接
        self.con = pymysql.connect(host="120.78.128.25",
                                   port=3306,
                                   user="future",
                                   password="123456",
                                   charset="utf8",
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
        # 创建一个游标对象
        self.cur = self.con.cursor()

    def find_all(self, sql):
        """
        查询sql语句返回的所有数据
        :param sql: 查询的sql
        :return: 查询到的所有数据
        """
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_one(self, sql):
        """
        查询sql语句返回的第一条数据
        :param sql: 查询的sql
        :type sql:str
        :return: sql语句查询到的第一条数据
        """
        self.cur.execute(sql)
        return self.cur.fetchone()

    def update(self, sql):
        """
        增删改操作的方法
        :param sql: 增删改的sql语句
        :return:
        """
        self.cur.execute(sql)
        self.con.commit()

if __name__ == '__main__':
    db = HandleMysql()

    sql = "SELECT * FROM futureloan.member LIMIT 10"

    res = db.find_one(sql)
    print(res)