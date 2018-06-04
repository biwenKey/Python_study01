#!/usr/bin/env python
# -*- coding:utf-8 -*-
tp01 = "i am {}, age {}, {}".format("seven", 18, 'alex')
print(tp01)
tp02 = "i am {}, age {}, {}".format(*["seven",18,'alex'])
print(tp02)
tp03 = "i am {0}, age {1}, really {0}".format("seven", 18, "hehe")
print(tp03)
tp04 = "i am {0}, age {1}, really {0}".format(*["seven", 18])
print(tp04)
tp05 = "i am {name}, age {age}, really {name}".format(name="seven", age=18)
print(tp05)
tp06 = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(tp06)