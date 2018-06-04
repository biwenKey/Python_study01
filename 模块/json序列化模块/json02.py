#!/usr/bin/env python
# -*- coding:utf-8 -*-
user_list = ["alex", "eric", "tomy"]
import json
s = json.dumps(user_list)
print(s, type(s))