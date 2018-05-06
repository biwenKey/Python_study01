#!/usr/bin/env python
# -*- coding:utf-8 -*-
dic = {"k1": "v1v1", "k2": [11, 22, 33, 44],"k3":"v"}

li = []
for i in dic.values():
    if len(i) > 2:
       # print(i)
        li.append(i)

print(li)


