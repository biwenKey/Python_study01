#!/usr/bin/env python
# -*- coding:utf-8 -*-

（1）方法1
asset_all = 0
car_list = []
#首先输入总资产
il = input("请输入总资产:")
asset_all = int(i1)
#列出所有商品
for i in goods:
print(i['name'], i[price])
#用户选择商品
当用户选择商品的时候我们应该将这个商品加入到购物车里面
while True:
i2 = input("请选择商品(Y/y结算):")
if i2 == "y":
break
for j in goods:
if j['name'] == i2:
# j = {"name": "电脑", "price": 1999}
print(j)
car_list.append(j)
print(car_list)
#当用用户选择商品的时候可以选择多个商品都加入到购物车，因此在以上代码可以加一个循环，加一个while True循环，到上面
#当用户在选择商品的时候选择了y，则下面就应该去结算了
all_price = 0
for item in car_list:
p = item['price']
all_price = all_price + p
print(asset_all, all_price)
if all_price > asset_all:
print("穷逼")
else:
print("购买成功")