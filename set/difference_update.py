#!/usr/bin/env python
# -*- coding:utf-8 -*-
se = {11,22,33}
be = {22,55}
#找se中存在，be中不存在的值，然后更新自己
se.difference_update(be)
print(se)
