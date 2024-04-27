# For Loop

# myList = ["banana", "mandarin", "cherry", "watermelon", "apple"]
# list
# myList = ("banana", "mandarin", "cherry", "watermelon", "apple")
# tuple
# myList = {"banana", "mandarin", "cherry", "watermelon", "apple"}
# set

# for x in myList:
#     if x == "mandarin":
#         break
#     print(x)

# for x in "apple":
#     print(x)

# for x in myList:
#     if x == "cherry":
#         continue
#     print(x)


# for x in range(3, 10, 2):
#     print(x)
#     if x == 7:
#         break
# else:
#     print("for loop done")

for x in range(2, 10):
    for y in range(2, 10):
        if (x == 8):
            continue
        print(x, '*', y, '=', x * y)
    print("=========================")
