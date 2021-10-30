# -*- coding:utf-8 -*-
N = int(input())
p, q = 2, N - 2
while p <= q:
    flag = True
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            flag = False
            break
    for j in range(2, int(q ** 0.5) + 1):
        if q % j == 0:
            flag = False
            break

    if flag == True:
        print('{} = {} + {}'.format(N, p, q))
        break
    p += 1
    q -= 1
