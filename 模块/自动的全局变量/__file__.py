#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
#print(__file__)
#print(os.path.dirname(__file__))
#for i in sys.path:
#    print(i)
#print(os.path.dirname(os.path.dirname(__file__)))
p1 = os.path.dirname(__file__)
p2 = "lib"
my_dir = os.path.join(p1,p2)
sys.path.append(my_dir)
import s2
s = s2.f2()
print(s)
print(my_dir)
print(p1)

