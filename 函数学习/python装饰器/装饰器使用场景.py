#!/usr/bin/env python
# -*- coding:utf-8 -*-

def outer(func):
    def inner():
        print("hello")
        print("hello")
        r = func()
        return r
        print("end")
        print("end")
    return inner


@outer
def f1():
    print("F1")

def f2():
    print("F2")

r = f1()
print(r)