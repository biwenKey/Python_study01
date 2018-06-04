#!/usr/bin/env python
# -*- coding:utf-8 -*-
s1 = '{"desc":"ssswdwdwwd","status":1000}'
import json
result = json.loads(s1)
print(result, type(result))

s2 = '[11,22,33,44]'
import json
result01 = json.loads(s2)
print(result01,type(result01))




