# -*- coding:utf-8 -*-
# Code by Aaron

# out put a random number.
import random
x = int(input('Input a small limitaion number:'))
y = int(input('Input a large limitaion number:'))
z = y - x
print('Circle %d times.' % z)
for i in range(z):
    print('% d times output a random number between %d and %d :'\
          % (i + 1, x, y), random.randint(x, y))