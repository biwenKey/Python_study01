#!/usr/bin/env python
# -*- coding:utf-8 -*-

tu = ("alec", " aric", "Alex", "Tony", "rain")
for i in tu:
    newsi =  i.strip()
    if (newsi.startswith("a") or newsi.startswith("A")) and newsi.endswith("c"):
        print(newsi)







