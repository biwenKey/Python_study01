#!/usr/bin/env python
# -*- coding:utf-8 -*-
def f1(p):
    print(p)
    if True:
        return p
    else:
        return False

r1 = f1({})

print(r1)
print(r1["k1"])

for key,vales in r1.items():
    print(key,":",vales)



