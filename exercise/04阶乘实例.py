# -*- coding:utf-8 -*-
# Code by Aaron

# 阶乘实例
def jiecheng():
    num = int(input('输入所要求取阶乘的正整数:'))
    if num < 0:
        print('负数没有阶乘,请输入一个正整数!!!')
        jiecheng()
    elif num == 0:
        print('%d的阶乘为:' % num, 1)
    else:
        result = 1
        for i in range(1, num+1):
            result *= i
        print('%d的阶乘为:' % num,result)

jiecheng()