#!/usr/bin/env python
# -*- coding:utf-8 -*-
a = "1 + 3"
print(a)
ret = eval("102 + 98 + 60")
print(ret)
ret01 = eval("a + 60", {"a":90})
print(ret01)
exec("for i in range(10):print(i)")