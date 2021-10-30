# -*- coding:utf-8 -*-
print('''[1] apple
[2] pear
[3] orange
[4] grape
[0] exit''')

nums = input().split()
count = 0

for num in nums:
    if count == 5:
        break
    if num == '0':
        break
    elif num == '1':
        print("price = 3.00")
    elif num == '2':
        print("price = 2.50")
    elif num == '3':
        print("price = 4.10")
    elif num == '4':
        print("price = 10.20")
    else:
        print("price = 0.00")
    count += 1

