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

a = {"apple", "banana", "cherry"}

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

a.remove("banana")
a.remove("banana")
a.discard("banana")
# b = a.pop()
print(a)
