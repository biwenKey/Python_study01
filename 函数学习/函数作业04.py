#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容
def f2(p):
    #jieguo = []
    for i in p:
        if i.isspace():
            #jieguo.append("确实是包含了空内容")
            print(i,"是空格")
        else:
            #jieguo.append("没有包含空内容")
            print(i)
    #return jieguo


f2(("women"," ","shabi"))

