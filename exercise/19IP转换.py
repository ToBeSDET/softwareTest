# -*- coding:utf-8 -*-
# Code by Aaron

# 将ip = '192.168.12.79'中的每个十进制转化成二进制,在将所有的二进制组成一个二进制
# 将所得的二进制转化为十进制

ip = '192.168.12.79'

each = ip.split('.')
result1 = []

for i in each:
    result1.append(bin(int(i)))

print(result1)

result2 = []
for j in result1:
    result2.append(j[2:])

print(result2)

# # 方法一
# x = ['0', '00', '000', '0000', '00000', '000000', '0000000', '00000000']
# for k in range(4):
#     if len(result2[k]) < 8:
#         result2[k] = x[(8-len(result2[k]))-1]+result2[k]

# 方法二
x = '0'
for k in range(4):
    while len(result2[k]) < 8:
        result2[k] = x + result2[k]

print(result2)
result3 = ''.join(result2)
print(result3)
print(int(result3, base=2))

# 下述语句等于print(int(result3, base=2))
x = 0
for i in range(len(result3)):
    if result3[i] == '1':
        x += 2**(len(result3)-i-1)
print(x)