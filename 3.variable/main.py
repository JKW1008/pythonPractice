# 변수
x = 10
print(type(x))  # int - integer

y = "Hello"
print(type(y))  # str - string

z = 3.3
print(type(z))


fruits = ["apple", "banana", "cherry"]

x, y, z = fruits
print(y)

x = "파이썬은 놀라워"
print(x)

x = "파이썬은"
y = "놀라워"
print(x, y)

z = x + " " + y
print(z)

x = 3
y = 4
z = x + y
print(z)

x = '3'
y = '4'
z = x + y
print(z)

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)
