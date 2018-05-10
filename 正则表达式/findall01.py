#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
#s = re.findall("","a2b3c4d5")
#print(s)
a = "alex"
n =re.findall("(\w)(\w)(\w)(\w)", a)
print(n)

n1 = re.findall("(\w)*",a)
print(n1)
