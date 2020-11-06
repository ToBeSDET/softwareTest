# -*- coding:utf-8 -*-
# Code by Aaron

# 插入排序

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [12, 11, 13, 5, 6, 1, 10]
print('原始数组:', arr)
insertionSort(arr)
print('排序后的数组:',arr)