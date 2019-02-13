#person = ["H.Duc", 24, "Hai Phong", 11, False, 430, True]

# person = {}
# print(person)
# print(type(person))

# person = {
#     "name": "H.Duc"
# }
# print(person)

person = {
    "name": "H.Duc",
    "age": 24,
    "Status": False,
    "location": "Hai Phong",
}

k = "zzzzzzzname"
if k in person:
    print(person[k])
else:
    print("Not found")

#print(person["location"])