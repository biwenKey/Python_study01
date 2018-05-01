#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

def f3(p):
    if len(p) > 2:
        print(p[0:2])
    else:
        print("列表的长度小于2")

f3([11,22])
