# -*- coding:utf-8 -*-
N = int(input())
if N < 1:
    print('Invalid value')
else:
    list = [1, 1]
    if N == 1:
        print('%11d' %list[0])
    elif N == 2:
        print("%11d%11d" %(list[0], list[1]))
    else:
        for i in range(2, N):
            num = list[N - 1] + list[N - 2]
            list.append(num)
        count = 0
        for i in range(N + 1):
            print("%11d" %list[i], end = '')
            count += 1
            if count % 5 == 0:
                print("")
        if count < 5:
            print('')
