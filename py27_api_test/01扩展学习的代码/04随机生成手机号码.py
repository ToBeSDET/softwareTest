"""
============================
Author:柠檬班-木森
Time:2020/3/26   21:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import random
from common.handle_db import HandleMysql

db = HandleMysql()


def random_phone():
    """生成一个数据库里面未注册的手机号码"""

    while True:
        phone = "155"
        for i in range(8):
            r = random.randint(0, 9)
            phone += str(r)
        sql = "SELECT * FROM futureloan.member WHERE mobile_phone={}".format(phone)
        res = db.find_count(sql)
        if res == 0:
            return phone


res = random_phone()
print(res)
