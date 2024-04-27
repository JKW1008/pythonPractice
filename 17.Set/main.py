# Set
# Unindexed
# Unchangeable
# Unordered
# Duplicates Not Allowed
# a = [] list
# a = () tuple

# a = {"apple", "banana", "cherry", True, False}
# print(type(a))

# a = set(('apple', 'banana', 'cherry'))
# print(a)
# print(type(a))

# a = {"apple", "banana", "cherry"}

# for x in a:
#     print(x)

# b = "mango" in a
# print(b)

# if "mango" in a:
#     print("yes a type of set in mango")

# a.add("mango")
# print(a)
# b = {"mango", "orange", "papaya"}
# a.update(b)
# print(a)

# a.remove("banana")
# a.remove("banana")
# a.discard("banana")
# b = a.pop()
# print(a)


# a = {"apple", "banana"}
# b = {"mandarin", "pear"}
# a.update(b)   스스로 변화
# c = a.union(b)  새로운 배열을 할당
# print(c)

# a.clear()
# b = a.copy()

# print(b)


# a = {"apple", "banana", "mango"}
# b = {"banana", "apple"}
# z = a.difference(b)
# a.difference_update(b)
# 차집합


# c = a.intersection(b)
# a.intersection_update(b)
# 교집합

# c = a.isdisjoint(b)

# c = a.issubset(b)
# c = a.issuperset(b)

a = {1, 2, 3}
b = {3, 4, 5}

# c = a.symmetric_difference(b)
a.symmetric_difference_update(b)
# 합집합 - 교집합

print(a)
