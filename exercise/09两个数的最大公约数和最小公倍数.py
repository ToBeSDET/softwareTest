# -*- coding:utf-8 -*-
# Code by Aaron

# 两个数的最大公约数和最小公倍数
num1 = int(input('请输入第一个数字:'))
num2 = int(input('请输入第二个数字:'))

if num1 > num2:
    re1 = num2
    re2 = num1
else:
    re1 = num1
    re2 = num2

# 最大公约数
for i in range(1, re1 + 1):
    if num1 % i == 0 and num2  % i == 0:
        result1 = i

# 最小公倍数
j = 1
while True:
    if (re2 * j) % re1 == 0:
        result2 = re2 * j
        break
    j += 1

print(num1, '和', num2, '的最大公约数为', result1)
print(num1, '和', num2, '的最小公倍数为', result2)