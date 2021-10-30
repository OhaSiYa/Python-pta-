# -*- coding:utf-8 -*-
#最大公约数的四种求法
#1.辗转相除法
M, N = map(int, input().split())
t1 = M % N
M1, N1 = M, N
while t1 != 0:
    M1, N1 = N1, t1
    t1 = M1 % N1
t2 = M * N / N1

print("%d %d" %(N1, t2))
