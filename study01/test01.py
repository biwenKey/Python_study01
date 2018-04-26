name = "jinbiwen"
print(name)


import copy
n1 = 123
print(id(n1))

n2 = copy.copy(n1)
print(id(n2))

n3 = n1
print(id(n3))