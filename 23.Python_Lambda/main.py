# Python Lambda
# lambda a : a * 10

# def y(a): return a * 2


# print(y(15))


# def x(a, b): return a * b


# b = x(11, 2)
# print(b)
# print(x(11, 2))

# def func1(n):
#     return lambda a: a * n


# my1 = func1(5)
# my2 = func1(10)
# my3 = func1(15)

# print(my1(2))
# print(my2(2))
# print(my3(2))

# [1, 3, 5, 7 ,9]

mylist = list(filter(lambda x: x % 2, range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]
print(mylist)
