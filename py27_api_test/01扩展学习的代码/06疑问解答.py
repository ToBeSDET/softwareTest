"""
============================
Author:柠檬班-木森
Time:2020/3/28   10:50
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
疑问点：
1、这行代码的意思
headers["Authorization"] = self.token
2、用户id替换的是字符串，请求的时候怎么变成数值的
case["data"].replace("#member_id#", self.member_id)

"""

# headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
#
# headers["Authorization"] = "dtdadfygbhlkltrsgyduhjaidfayiujnfghjkl"
#
# print(headers)

data = '{"member_id": #member_id#,"amount":600}'
data = data.replace("#member_id#", "281")
print(eval(data))