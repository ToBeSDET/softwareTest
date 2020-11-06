# -*- coding:utf-8 -*-
# Code by Aaron

# 选择排序
a = [64, 25, 12, 22, 11]
print('排序前的数组:', a)

for i in range(len(a)):
    min_idx = i
    for j in range(i + 1, len(a)):
        if a[min_idx] > a[j]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

print('排序后的数组:', a)