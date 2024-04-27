# if statement

a = 290
b = 310
c = 320
# if a < b:
#     print("a is less then b")
# elif a == b:
#     print("a is same b")
# elif a >= b:
#     print("a is bigger then b or a is same b")
# else:
#     print("a is bigger then b")

# if a > b:
#     print("a is bigger then b")

# Short Hand If .. Else
# print("a is bigger then b") if a > b else print("b is bigger then a")

# print("A") if a > b else print("=") if a == b else print("B")

# if a > b and a > c:
#     print("a is biggest")
# else:
#     print("a was not biggest")

# if a > b or a > c:
#     print("a is not smallest")
# else:
#     print("a is smallest")

# if not a > b:
#     print("a is not bigger then b")

# Nested If

x = 3

if x > 3:
    pass

if x > 5:
    print("x is bigger then 5,")
    if x > 20:
        print("x is bigger then 20.")
    else:
        print("But smaller then 20")
else:
    print("x is same 5 or smaller")
    # pass
