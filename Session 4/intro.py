#person = ["H.Duc", 24, "Hai Phong", 11, False, 430, True]

# person = {}
# print(person)
# print(type(person))

# person = {
#     "name": "H.Duc"
# }
# print(person)

# person = {
#     "name": "H.Duc",
#     "age": 24,
#     "Status": False,
#     "location": "Hai Phong",
# }

# person["Friend_count"] = 450

# print(person)
# k = "zzzzzzzname"
# if k in person:
#     print(person[k])
# else:
#     print("Not found")

#print(person["location"])

# k= "location"

# if k in person:
#     print(person[k])
# else:
#     print("Not found")

# person = {
#     "name": "H.Duc",
#     "age": 24,
#     "Status": False,
#     "location": "Hai Phong",
# }

# person["age"] += 2

# del person["age"]

# print(person)

p0 = {
    "name": "H.Duc",
    "age": 24,
    "Status": False,
    "location": "Hai Phong",
}

p1 = {
    "name": "Hoang",
    "age": 21,
    "location": "Hanoi",
    "status": "Suyt"
}

p2 = {
    "name": "Son",
    "age": 18,
    "location": "Hung Yen",
    "status": True
}

p_list = [
    {
        "name": "H.Duc",
        "age": 24,
        "Status": False,
        "location": "Hai Phong"
    },
    p1,
    p2
]



# p_list.append(p0)
# p_list.append(p1)
# p_list.append(p2)


print(*p_list, sep="\n")
# print(p_list[1])
# print(p_list[1]["status"])

# for p in p_list:
#     print(p["name"])

# print(p_list[0]["location"])


# for fav in person["favs"]:
# print(fav)

# print(person["favs"][1])

# for i in person.keys():
#     print(i, person[i])

# for v in person.values():
#     print(v)

# for (k, v) in person.items():
#     print(k,v)

# print(*person.keys(), sep = "\n")