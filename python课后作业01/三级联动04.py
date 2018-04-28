#!/usr/bin/env python
# -*- coding:utf-8 -*-

dic = {
    "河北":{
         "石家庄":["鹿泉","藁城", "元氏"],
         "邯郸": ["永年", "涉县", "磁县"],
     },
    "河南": {
       "郑州": ["中原", "金水", "惠济"],
       "开封": ["龙亭", "鼓楼", "顺河回族"],
     },
    "山西": {
        "太原": ["小店", "晋源", "尖草坪"],
        "运城": ["盐氏", "盐邑", "苦城"],
     },
}


while True:
    for i in dic:
        print(i)
    v1 = input("请输入你想要查询的省份:")
    if v1 not in dic.keys():
        print("你输入的省份有误！请重新选择。")
        continue
    else:
        for v2 in dic[v1]:
            print(v2)
        v3 = input("请输入你想要查询的市:")
        if v3 not in dic[v1].keys():
            print("你输入的市有误，请重新输入。")
            exit()
        else:
            for v4 in dic[v1][v2]:
                print(v4)
    print("==========================")







