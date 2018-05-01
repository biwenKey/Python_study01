#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

def fun01(p):
    num = 0
    letter = 0
    space = 0
    qita = 0
    for i in p:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            letter += 1
        elif i.isspace():
            space += 1
        else:
            qita += 1

    return (num,letter,space,qita)
ret = fun01("www swsdwdw wdwd w333 666 444   ")
print(ret)





