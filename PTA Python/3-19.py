# -*- coding:utf-8 -*-
N = int(input())
List = []
for i in range(N):
    str = input()
    List.append(str)

max = len(List[0])
index = 0
for i in range(1, N):
    if max < len(List[i]):
        max = len(List[i])
        index = i

print('The longest is:', List[index])
