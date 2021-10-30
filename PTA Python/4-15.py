# -*- coding:utf-8 -*-
x = int(input())
#三种硬币的个数
num1, num2, num3, = int(x / 5), int(x / 2), int(x)
count = 0
for i in range(num1, 0, -1):
    for j in range(num2, 0, -1):
        for k in range(num3, 0, -1):
            price = 5 * i + 2 * j + k
            total = i + j + k
            if price == x:
                print(
                    "fen5:{}, fen2:{}, fen1:{}, total:{}".format(i, j, k, total)
                )
                count += 1

print("count =", count)
