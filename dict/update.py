user_info = {
    "name": "alex",
    "age": 73,
    "gender": "M"
}

print(user_info.setdefault("shengao"))
print(user_info)
test = {"shengao":170}
user_info.update(test)

print(user_info)

del user_info["shengao"]
print(user_info)

dic01 = {"k1":123,"k2":566,"k3":789}
n = dic01.fromkeys(["k1","k2","k3"],[])
print(n)

n["k1"].append("x")
print(n)





