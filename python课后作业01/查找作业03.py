#!/usr/bin/env python
# -*- coding:utf-8 -*-

dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alec", "k4": "Tony"}
#for k,v in dic.items():
#    print(k,":",v)


for i in dic.values():
#    print(i)
    newdic = i.strip()
    if (newdic.startswith("a") or newdic.startswith("A")) and newdic.endswith("c"):
        print(newdic)



