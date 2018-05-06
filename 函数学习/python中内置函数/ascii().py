#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Foo:
    def __repr__(self):
        return "hello"

obj = Foo()
r = ascii(obj)
print(r)

#li = list()
#r = ascii(li)
print(r)