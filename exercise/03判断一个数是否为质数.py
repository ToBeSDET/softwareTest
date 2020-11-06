# -*- coding:utf-8 -*-
# Code by Aaron

# 判断一个数是否为质数
num = int(input('输入一个整数:'))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print('%d不是质数' % num)
            print('%d * %d = %d' % (i, num//i, num))
            break
    else:
        print('{}是质数'.format(num))
else:
    print('%d不是质数' % num)


# 输出指定范围内的所有质数
def zhishu():
    low = int(input('输入指定范围的下限:'))
    high = int(input('输入指定范围的上限:'))
    if high < low:
        print('输入的上限小于下限,请重新输入')
        zhishu()
    if high < 1:
        print('输入的上限必须大于等于1,请重新输入')
        zhishu()
    x = []
    if low <= 1:
        if low == 1:
            x.append(low)
        for i in range(2, high + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                x.append(i)
    else:
        for i in range(2, high + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                x.append(i)
    print('[{0}, {1}]之间的质数有:\n'.format(low, high), x)

zhishu()