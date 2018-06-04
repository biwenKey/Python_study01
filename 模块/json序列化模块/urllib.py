#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
from urllib import request
req = urllib.request.Request('http://ww.weather.com.cn/data/sk/101050101.html')
r = urllib.request.urlopen(req)
result = str(r.read(), encoding='utf-8')

import json
dic = json.loads(result)
print(type(dic), dic)