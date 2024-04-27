# Tuple
# 1) 값을 변경할 수 없다.
# 2) 중복 데이터를 허용한다.
# 3) 순서가 있다.

a = tuple(("사과", "오렌지", "망고", "딸기", 1, True, False))
# print(a)
# print(type(a))
# print(a[1:3])
# print(len(a))


# if "사과" in a:
#     print("yes, apple in a type tuple")
# b = list(a)
# b.append("cherry")
# a = tuple(b)
# print(a)

a += ("체리",)
# print(a)

# (a1, a2, a3, a4, a5, a6, a7, a8) = a
# print(a1)
# print(a2)
# print(a3)

# for x in a:
#     print(x)

# for i in range(len(a)):
#     print(a[i])

# print(range(len(a)))
b = a * 2
# print(b)
cnt = b.count("사과")
# print("사과는" + str(cnt) + "개 있습니다.")
print("사과는 {0}개 있습니다.".format(cnt))
