#!/usr/bin/env python
# -*- coding:utf-8 -*-
def outer(func):
    def inner(*args,**kwargs):
        print("我曹")
        print("我曹")
        r = func(*args,**kwargs)
        print(456)
        return r


    return  inner






@outer
def f1(*args,**kwargs):
    print("非常复杂")
    print(args)
    print(kwargs)
    if args and kwargs:
        return True
    else:
        return False

r = f1(11,22,key1=123,key2=456)
print(r)

