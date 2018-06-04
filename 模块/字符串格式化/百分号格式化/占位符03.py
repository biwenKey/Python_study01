#!/usr/bin/env python
# -*- coding:utf-8 -*-
s1 = "i am %(n1)+10s asdddwsdssdsssd" % {"n1":"alex"}
print(s1)
s2 = "i am %(n1)+10d dsdsdsdsdsdsdss" % {"n1": -191}
print(s2)
s3 = "i am %(n1)010d dsdsdsdsdsdsdss" % {"n1": 1910}
print(s3)