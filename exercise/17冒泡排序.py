# -*- coding:utf-8 -*-
# Code by Aaron

# 冒泡排序

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
print('排序前的数组:', arr)
bubbleSort(arr)
print('排序后的数组:', arr)