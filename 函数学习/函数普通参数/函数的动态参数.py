#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""
def f1(**a):
    print(a,type(a))

f1(k1=123,k2=456)

def f1(*a, **aa):
    print(a,type(a))
    print(aa,type(aa))

f1(11,22,33, k1=123, k2=456)


def f1(p, *a, **aa):
    print(p,type(p))
    print(a, type(a))
    print(aa,type(aa))

f1(11,22,33,k1=123,k2=345)

def f1(*args):
    print(args,type(args))

#li = (11,22,33,44)
li = ["jinbiwen",123,"women"]
f1(li)
f1(*li)
"""
def f1(**kwargs):
    print(kwargs,type(kwargs))


dic = {"k1":123,"k2":456,"k3":789}

f1(**dic)
f1(k1=dic)
