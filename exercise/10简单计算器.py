# -*- coding:utf-8 -*-
# Code by Aaron

# 简单计算器
def add(x, y):
    '''相加'''
    return x + y

def subtract(x, y):
    '''相减'''
    return x - y

def mutiply(x, y):
    '''相乘'''
    return x * y

def divide(x, y):
    '''相除'''
    return x / y

print('''\
选择运算符:
1、相加
2、相减
3、相乘
4、相除
''')

def input1():
    choice = input('请输入你的选择1/2/3/4:')
    if choice not in ['1', '2', '3', '4']:
        print('非法输入,请重新输入!')
        input1()
    else:
        num1 = int(input('请输入第一个数字:'))
        num2 = int(input('请输入第二个数字:'))
        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', mutiply(num1, num2))
        else:
            print(num1, '/', num2, '=', divide(num1, num2))


input1()