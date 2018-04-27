#!/usr/bin/env python
# -*- coding:utf-8 -*-
se = {11,22,33}
be = {22,95,"随便"}
ret = se.intersection(be)
print(ret)
#取交集并且更新自己为这个交集所得的值
se.intersection_update(be)
print(se)
