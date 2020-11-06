# -*- coding:utf-8 -*-
# Code by Aaron
import random

num = random.randint(1,100)
print('在1-100之间猜猜我心里想的数，你有三次机会哦！')

count = 1
while count <= 3:
    guess = int(input('\n请输入你猜的数：'))
    if guess > num:
        print('\n你输入的数大了一些哦！')
    elif guess < num:
        print('\n你输入的数小了一些哦！')
    else:
        print('\n恭喜你猜对了！')
        break
    if count == 3:
        choice = input('\n很遗憾你已经用完三次机会了，请选择是否继续（Y/N)：')
        choice = choice.upper()
        if choice == 'Y':
            count = 1
            continue
        elif choice == 'N':
            break
    count += 1

