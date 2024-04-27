# Dictionary
# 3.6 unordered
# 3.7 ordered

a = {
    "name": "smith",
    "age": 19,
    # "address": "Banpo Dong Seocho Gu Seoul",
    "address": "Dachi Dong Kangnam Gu Seoul",
    "hobby": ["Flower Art", "Movie", "Climing"]
}

# print(a)
# print(type(a))
# print(a["name"])
# print(a["age"])
# print(a["address"])
# print(len(a))

# b = dict(name="John", age=36)
# print(b)

# b = a["address"]
# print(b)

# b = a.get("address")
# print(b)

# b = a.keys()
# print(b)

# a["age"] = 20
# a.update({"age": 21})
# print(a)

# a["color"] = ["red", "blue", "green"]
# a.update({"color": ["red", "blue", "green"]})
# print(a)

# a.pop("age")
# c = a.pop("age")
# print(c)

# a.popitem()
# a.popitem()
# c = a.popitem()

# print(c)
# print(type(c))

# del a["hobby"]
# del a

# a.clear()
# print(a)

# for x in a:
#     print(a[x])

for x in a:
    print(a.get(x))
