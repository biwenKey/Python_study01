#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

def f4(p):
    li = []
    for i in range(len(p)):
        if i % 2 == 1:
            li.append(p[i])

    return li

ret = f4([11,22,33,44,55,66,77,88])
print(ret)





