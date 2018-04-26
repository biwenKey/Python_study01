s1 = "李露"
li = list(s1)
print(li)

t2 = ("jinbiwen01","jinbiwen02","jinbiwen03")
l2 = list(t2)
print(l2)

t3 = {"k1":"alex",
      "k2":"seven"
      }
#l3 = list(t3)
#print(l3)
l3 = list(dict.values(t3))
print(l3)
l4 = list(dict.items(t3))
print(l4)


