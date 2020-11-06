# -*- coding:utf-8 -*-
# Code by Aaron

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{0}*{1}={2}'.format(j, i, i * j), end='\t')
    print()

# 一行代码写出九九乘法表
[(print('%d*%d=%d' % (j, i, i * j), end='\t') if i != j else print('%d*%d=%d' % (j, i, i * j))) for i in range(1, 10)
 for j in range(1, 10) if j <= i]

# 一行代码写出九九乘法表
[(print('%d*%d=%d' % (j, i, i * j), end='\t') if i != j else print('%d*%d=%d' % (j, i, i * j))) for i in range(1, 10)
 for j in range(1, i + 1)]

# 一行代码写出九九乘法表
print('\n'.join(['\t'.join(['%d*%d=%d' % (j, i, i*j) for j in range(1, i+1)]) for i in range(1, 10)]))

