#!/usr/bin/env python
# -*- coding:utf-8 -*-

#输出商品列表，用户输入序号，显示用户选中的商品
#商品 li = ["手机", "电脑", '鼠标垫', '游艇']
li = ["手机", "电脑", '鼠标垫', '游艇']
print(len(li))
print(li[3])
for i,j in enumerate(li,1):
    print(i,j)


num = input("请输入商品序号:")
num = int(num)
if num > 0 and num <= len(li):
    print(li[num - 1])
else:
    print("你输入的商品不存在")




