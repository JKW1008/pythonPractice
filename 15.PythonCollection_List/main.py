# List, Tuple, Set, Dictionary
# List
# 1) 중복허용
# 2) 순서가 있음
# 3) 리스트는 변경이 가능
# a = ["apple", "banana", "cherry", "apple"]
# print(a)
# a[0] = "kiwi"
# print(a)

# print(a[1:3])
# b = a[1:3]
# print(b)
# print(type(a))

# a = ["사과", "바나나", "체리", "오렌지", "키위", "망고"]
# a[1:3] = ["딸기"]
# a.insert(1, "딸기")
# a.remove("사과")
# a.pop(1)
# del a[0]
# a.clear()

# print(a)

# for x in a:
#     print(x)

# a.sort()
# print(a)

# b = [100, 200, 10, 30, 90]
# b.sort(reverse=True)
# print(b)

# b = a.copy()

# print(a)
# b[0] = "apple"
# print(b)

# b = list(a)
# b[0] = "apple"
# print(b)

# a = ["apple", "banana"]
# b = ["cherry", "mango"]

# c = a + b
# for x in b:
#     a.append(x)
# print(a)

# a.extend(b)

# print(a)

a = ["apple", "banana", "apple", "mango"]
# print(a.count("apple"))
a.reverse()
print(a)
