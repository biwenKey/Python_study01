user_info = {
    "name": "alex",
    "age": 73,
    "gender": "M"
}

#for i in user_info.keys():
#    print(i)
#for i in user_info.values():
#    print(i)

for k,v in user_info.items():
    print(k,":",v)

user_info.clear()
print(user_info)

