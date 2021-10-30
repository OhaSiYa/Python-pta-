# -*- coding:utf-8 -*-
number = input()
List = []
for num in number[::-1]:
    List.append(num)
index = 0
while index < len(number):
    if number[index] == '0':
        index += 1

for i in range(index, len(List)):
    print("%s" %List[i])