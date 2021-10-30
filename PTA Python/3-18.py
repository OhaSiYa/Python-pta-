# -*- coding:utf-8 -*-
str = input()
List = []
count = 0
for chara in str:
    if chara.isalpha() and (chara.lower() not in List) and (chara.upper() not in List):
        List.append(chara)
        count += 1

if count < 10:
    print('not found')
else:
    for i in range(len(List)):
        print(List[i], end = '')
