#!/usr/bin/env python
# -*- coding:utf-8 -*-


#购物车
#功能要求：
#要求用户输入总资产，例如：2000
#显示商品列表，让用户根据序号选择商品，加入购物车
#购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
#附加：可充值、某商品移除购物车
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

gouwuche = []
for i in goods:
    print(i["name"],i["price"])
qian = input("请输入您想要话费的金额:")
qian = int(qian)

while True:
    xuanze = input("请您选择你要购买的产品:")
    for item in goods:
        if item["name"] == xuanze:
            if qian >

            gouwuche.append(xuanze)
            print(gouwuche)

        else:
            print("您输入的产品有误，请您重新选择!")
            continue





