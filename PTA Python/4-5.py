# -*- coding:utf-8 -*-
N = int(input())
sum, fenmu = 1, 1
for i in range(1, N + 1):
    fenmu *= i
    sum += 1 / fenmu

print("%.8f" %sum)