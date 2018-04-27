#!/usr/bin/env python
# -*- coding:utf-8 -*-
#查找
#查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
#    li = ["alec", " aric", "Alex", "Tony", "rain"]
#    tu = ("alec", " aric", "Alex", "Tony", "rain")
#    dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}
newsli = []
li = [" alec ", " aric", "Alec", "Tony", "rain"]
print(li)
for i in li:
    wocao = i.strip()
    if (wocao.startswith("a") or wocao.startswith("A")) and wocao.endswith("c"):
        newsli.append(wocao)

print(newsli)


#下面这种写法是不正确的，有bug
#for i in li:
#    news = i.strip()
#    if news.startswith('a') or news.startswith('A') and news.endswith('c'):
#        print(i)









