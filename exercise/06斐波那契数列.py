# -*- coding:utf-8 -*-
# Code by Aaron

# 斐波那契数列
def feibonacci(n):
    a, b = 0 ,1
    x = []
    x.append(a)
    while True:
        if b <= n:
            x.append(b)
            a, b = b, a+b
        else:
            break
    print('%d范围内的斐波那契数列为:\n' % n, x)

num = int(input('请输入一个大于零的整数:'))
feibonacci(num)