#!/usr/bin/env python
# -*- coding:utf-8 -*-
def outer(func):
    def inner():
        print(123)
        ret = func()
        print(456)
        return ret
    return inner



@outer
def index():
    print("非常复杂")
    return True

s = index()
print(s)

