# -*- coding:utf-8 -*-
str = input()
List = []
for chara in str:
    if ord('A') <= ord(chara) <= ord('Z') and chara not in List:
        List.append(chara)

if len(List) == 0:
    print('Not Found')
else:
    for chara in List:
        print(chara, end = '')
