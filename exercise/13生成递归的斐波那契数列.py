# -*- coding:utf-8 -*-
# Code by Aaron

# 生成递归的斐波那契数列
def feibonacci(n):
    if n <= 1:
        return n
    else:
        return (feibonacci(n - 1) + feibonacci(n - 2))


n = int(input('你需要生成几项斐波那契数列:'))
result = []
for i in range(n):
    result.append(feibonacci(i))
print(result)
