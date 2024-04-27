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
def my_funct(**kargs):
    print("Hello, my name is {}".format(kargs["name"]))
    print("and my age is {}".format(kargs["age"]))


my_funct(name="길동", age="19")
