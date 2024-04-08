# String method - format()

# age = 10
# age = str(19)
# a = "제 이름은 왕초보 입니다. 나이는 {}세 입니다."
# b = a.format(age)
# b = "제 이름은 왕초보입니다. 나이는 " + age + "세 입니다."

# print(b)


# name = "홍길동"
# age = 19

# text = "저는 {} 이고, 나이는 {} 세 입니다."
# text = "저는 {1} 이고, 나이는 {0} 세 입니다."
# text = "저는 {name} 이고, 나이는 {age} 세 입니다."

# b = text.format(name, age)
# b = text.format(name = "홍길동", age = 19)


# print(b)

# txt = "저는 {:<6} 마리의 닭을 기릅니다." # 좌측정렬
# txt = "저는 {:>6} 마리의 닭을 기릅니다." # 우측정렬
# txt = "저는 {:^6} 마리의 닭을 기릅니다." # 가운데 정렬
# txt = "저는 {:=6} 마리의 닭을 기릅니다."


# print(txt.format(10))
# print(txt.format(100))
# print(txt.format(1000))
# print(txt.format(10000))
# print(txt.format(100000))

# print(txt.format(12))
# print(txt.format(123))
# print(txt.format(1234))
# print(txt.format(12345))
# print(txt.format(123456))

# print(txt.format(-12))
# print(txt.format(-123))
# print(txt.format(-1234))
# print(txt.format(-12345))
# print(txt.format(-123456))

# txt = "오늘 기온은 최고 {:+}, 최저 {:+} 가 예상됩니다."
# txt = "오늘 기온은 최고 {:-}, 최저 {:-} 가 예상됩니다."

# print(txt.format(10, -5))

# txt = "저는 {:_} 를 가지고 있습니다"

# print(txt.format(10000000000000))


# txt = "숫자 {0}는 이진수로 {0:b} 입니다."
# txt = "저는 사과를 {:d} 개를 가지고 있어요."

# print(txt.format(1))
# print(txt.format(2))
# print(txt.format(3))
# print(txt.format(4))
# print(txt.format(5))

# print(txt.format(0b11)) # 2진수 -> 10진수
# print(txt.format(0o11)) # 8진수 -> 10진수

txt = "저의 타율은 {:.1%}입니다."
print(txt.format(0.333))
