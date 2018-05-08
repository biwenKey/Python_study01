#!/usr/bin/env python
# -*- coding:utf-8 -*-

def outer(func):
    def inner(a1,a2):
        print("wocao")
        print("wocao")
        r = func(a1,a2)
        print(r)
        print("end")
        print("end")
        return r





    return inner

@outer
def index(a1,a2):
    print("非常复杂")
    return a1 + a2

s = index(1,2)
print(s)