# -*- coding:utf-8 -*-
"""
作者：肖思洋
广西大学计算机与电子信息学院
"""
str = input()
left, right = 0, len(str) - 1
flag = True
while left < right:
    if str[left] != str[right]:
        flag = False
        break
    left += 1
    right -= 1

print(str)
if flag == False:
    print('No')
else:
    print("Yes")