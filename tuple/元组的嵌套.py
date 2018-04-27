#!/usr/bin/env python
# -*- coding:utf-8 -*-
t1 = (11,22,33)
t2 = (11,22,["alex",{"k1":"v1","k2":"v2"}])
s = t2[2][1]["k2"]
print(s)
t2[2][1].update({"k3":123})
print(t2)
##给字典添加更新的两种方式
dic = {"k1":"v1"}
dic.update({"k2":123})
print(dic)
dic["k3"] = 456
print(dic)





