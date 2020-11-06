# -*- coding:utf-8 -*-
# Code by Aaron

'''
读取文件数据并转化为特定格式
'''

def read():
    with open('a.log', mode='w', encoding='utf-8') as f:
        content = 'aaron|123|18\neric|456|19'
        f.write(content)

    with open('a.log', mode='r', encoding='utf-8') as f:
        y = []
        z = []
        h = ['name', 'pwd', 'age']
        x = f.read().split('\n')
        for i in x:
            y.append(i.split('|'))
        for i in x:
            z.append({h[j]: i.split('|')[j] for j in range(3)})
    print(x)
    print(y)
    print(z)

read()