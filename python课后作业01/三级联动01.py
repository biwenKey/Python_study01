#!/usr/bin/env python
# -*- coding:utf-8 -*-

#用户交互，显示省市县三级联动的选择
#dic = {
#    "河北": {
#        "石家庄": ["鹿泉", "藁城", "元氏"],
#        "邯郸": ["永年", "涉县", "磁县"],
#    },
#    "河南": {
#        "郑州": ["不知道", "少林寺", "嵩山"],
#        "开封": ["包拯", "展昭", "威士忌"],
#    },
#    "山西": {
#        "太原": ["xxx", "ooo", "小店"],
#        "运城": ["更不知道了", "999", "哈尔冰啤酒"],
#    },
# }



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

print(dic["河北"])

for i in dic:
    print(i)

i1 = input("请输入你要查询的身份:")
a = dic[i1]
for j in a:
    print(j)
i2 = input("请输入你要查询的市:")
b = dic[i1][i2]
#print(b)
for w in b:
    print(w)





