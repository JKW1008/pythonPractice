# function

# def my_funct(name, age):
#     print("Hello, my name is {}".format(name))
#     print("and my age is {}".format(age))


# my_funct("gildong", 19)
# my_funct("gilsun", 18)


# my_funct(name="gildong", age=19)
# my_funct(name="gilsun", age=18)

# Arbitrary Arguments
# def my_funct(*args):
#     print("Hello, my name is {}".format(args[0]))
#     print("and my age is {}".format(args[1]))


# my_funct("길동", 19)
# my_funct("길순", 17)


# Arbitrary Keyword Arguments
# def my_funct(**kargs):
#     print("Hello, my name is {}".format(kargs["name"]))
#     print("and my age is {}".format(kargs["age"]))


# my_funct(name="길동", age="19")


# default Parameter value
# def my_funct(country="한국"):
#     print("저는 {}인 입니다".format(country))


# my_funct("미국")
# my_funct("스위스")
# my_funct()

# def my_funct(aaa):
#     print(aaa)

# def my_funct(aaa):
#     for x in aaa:
#         print(x)


# my_funct(["한국", "미국", "중국"])

# a = ("한국", "미국", "중국")

# my_funct(a)

# def my_funct(aaa):
#     return aaa * 2


# b = my_funct(30)
# print(b)


# def my_funct(aaa):
#     pass


# b = my_funct(30)
# print(b)

# 위치 def my_funct(aaa, bbb, ccc, /)
# def my_funct(aaa, /):
#     pass

# b = my_funct(1)

# 키워드 *,
# 키워드 def my_funct(*, aaa, bbb, ccc)

# def my_funct(*, aaa):
#     pass


# b = my_funct(aaa=1)


# print(b)


# def my_funct_keyword(*, x):
#     print(x)


# my_funct_keyword(x=3)


# def my_funct_position(x, /):
#     print(x)


# my_funct_position(3)


# def my_funct_keyword_position(a, b, /, *, c, d):
#     print(a, b, c, d)


# my_funct_keyword_position(1, 2, c=2, d=4)


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
