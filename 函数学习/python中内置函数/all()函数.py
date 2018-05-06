#!/usr/bin/env python
# -*- coding:utf-8 -*-
r = all([True,True])
print(r)
r1 = all(["123","",[],"1"])
print(r1)
i = any([None,"",[],{},()])
print(i)
i1 = any([None,123,[],{},()])
print(i1)