#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
shangping_list = [
    ("电脑",5000),
    ("手机",1800),
    ("耳机",200),
]
gouwuche = []
salary = input("请输入你此次想花费的金额:")
if salary.isdigit():
    salary = int(salary)
else:
    print("请输入数字")
    exit()
while True:
    for index,item in enumerate(shangping_list):
        print(index,item)
    bianhao = input("请输入你要购买的商品的编号:")
    if bianhao.isdigit():
        bianhao = int(bianhao)
        if bianhao <= len(shangping_list) and bianhao >= 0:
            goumai = shangping_list[bianhao]
            if salary >= goumai[1]:
                salary -= goumai[1]
                gouwuche.append(goumai[0])

                print("你购买的商品",goumai[0],"已经加入到购物车，你的余额为",salary)
                #print(gouwuche)
            else:
                print("你的余额不足买不起",goumai[0])
                time.sleep(3)
        else:
            print("你输入的编号提示没有此产品，请重新选择")
            time.sleep(3)
    elif bianhao == "q":
        print("--------------你购买的商品列表----------")
        for p in gouwuche:
            print(p)
        print("你的账户余额为",salary)
        exit()
    else:
        print("你输入的编号无效，请你重新输入商品编号")
        time.sleep(3)
