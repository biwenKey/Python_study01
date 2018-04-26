user_info = {
    "name": "alex",
    "age": 73,
    "gender": "M"
}

for k,v in user_info.items():
    print(k,":",v)

user_info.clear()
print(user_info)