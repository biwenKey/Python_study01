user_info = {
    "name": "alex",
    "age": 73,
    "gender": "M"
}

#ret = "age" in user_info.keys()

#print("age" in user_info.keys())
#print("alex" in user_info.values())
#ret = "age"  in user_info.keys()
#if ret == True:
#    print(user_info["age"])
#else:
#    print()

wocao = "age111"

ret = wocao in user_info.keys()

if ret == True:
    print(user_info[wocao])
else:
    haha = user_info.get("wocao", 123)
    print(haha)


