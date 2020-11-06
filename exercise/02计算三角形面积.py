# -*- coding:utf-8 -*-
# Code by Aaron

# calculate the area of a triangle
a = float(input('input one edge of a triangle:'))
b = float(input('input another edge of the triangle:'))
c = float(input('input the last one edge of the triangle:'))

s = (a + b + c)/2
area = (s * (s - a ) * (s - b) * (s - c)) ** 0.5

print('The area of the triangle is {}'.format(area))