#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
dic = {"k1": "v1v1", "k2": [11, 22, 33, 44],"k3":"v3"}
#PS: 字典中的value只能是字符串或列表
#方式一：
def f7(p):
    dic01 = {}
    for k,v in p.items():
        if len(v) > 2:
            dic01[k] = v[0:2]
    else:
           dic[k] = v

    return dic01

ret = f7(dic)
print(ret)


#方式二：
def f7_02(args):
    for key,value in args.items():
        if len(value) > 2:
            args[key] = value[0:2]
        else:
            args[key] = value


f7_02(dic)
print(dic)






