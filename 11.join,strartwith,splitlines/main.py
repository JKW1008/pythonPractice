# join(), startwith(), splitlines()

# myList = ["010-111-1111", "010-222-2222", "010-333-3333", "010-444-4444"]

# rs = "\n".join(myList)

# print(rs)

# a = "안녕하세요. 왕초보 홈페이지 만들기 채널입니다."

# rs = a.startswith("안녕")

# print(rs)

# a = "안녕하세요.\n반갑습니다.\n다음에 또만나요."

a = """\
안녕하세요
반갑습니다
다음에 또 만나요\
"""

rs = a.splitlines()
print(rs)
