# -*- coding:utf-8 -*-
# Code by Aaron


# 十进制转二进制
num = int(input('输入一个数字:'))
dec = abs(num)
x =[]
while True:
    n1 = 0
    while 2**n1 <= dec:
        n1 += 1
    n1 -= 1
    x.append(n1)
    dec = dec - 2**n1
    if dec <= 0:
        break
print(x)
m = max(x)
s = []
for i in range(m+1):
    if i in x:
        s.append('1')
    else:
        s.append('0')
print(s)
s.reverse()
print(s)
if num > 0:
    result = '0b'
    for i in s:
        result += i
elif num < 0:
    result = '-0b'
    for i in s:
        result += i
else:
    result = '0b0'
print('%d 的二进制为: %s' % (num, result))
print(num, '的二进制为:', bin(num))
print(num, '的八进制为:', oct(num))
print(num, '的十六进制为:', hex(num))