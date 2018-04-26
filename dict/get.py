user_info = {
    "name": "alex",
    "age": 73,
    "gender": "M"
}

va1 = user_info.get("age")
print(va1)
va2 = user_info.get("age111")
print(va2)

print(user_info["age"])
#print(user_info["age111"])
va3 = user_info.get("age111","int,s null")
print(va3)
print(user_info)