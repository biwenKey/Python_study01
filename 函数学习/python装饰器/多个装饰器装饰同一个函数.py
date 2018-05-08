#!/usr/bin/env python
# -*- coding:utf-8 -*-


def outer01(func):
    def inner(*args,**kwargs):
        print("我们都错了")
        s = func(*args,**kwargs)
        print("wocao")
        return s
    return inner

def outer02(func):
    def inner(*args,**kwargs):
        print("打倒日本帝国主义")
        print("打倒日本帝国主义")
        s = func(*args,**kwargs)
        print("打倒老美")
        print("打倒老美")
        return s
    return inner
@outer01
@outer02
def index(*args,**kwargs):
    print("我们都是中国人")
    print(args,kwargs)
    if args and kwargs:
        return True
    else:
        return False

w = index(11,22,333,key01=789,key02=123)
print(w)
