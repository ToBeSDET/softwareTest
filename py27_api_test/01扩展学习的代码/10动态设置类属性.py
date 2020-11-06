"""
============================
Author:柠檬班-木森
Time:2020/4/7   20:14
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


class EnvData:
    """定义一个类，用来保存用例执行过程中，提取出来的数据"""
    pass


data = {"member_id": 188, "mobile_phone": "13345677654"}

token = "fgshbamk'fnbaghjqawte27yuiepok[qla,mfntagdhjka,mfca789p"

# 动态的设置类属性
setattr(EnvData,"member_id",188)
setattr(EnvData,"token",token)
setattr(EnvData,"mobile_phone","13345677654")


# 获取类属性
print(EnvData.member_id)
print(getattr(EnvData,"member_id"))