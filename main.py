"""1masala"""

# with open("fayl.txt", "r") as file:
#     data = file.read()
#     word_count = len(data.split())
#     print(word_count)

"""2masala"""


# with open("fayl.txt", "r") as file:
#     data = file.read()
#     max = ""
#     for i in data.split():
#         if len(max) < len(i):
#             max = i

#     print(max)


"""3masala"""

# my_list = [1, 2, 3, 1, 4, 5, 6, 2, 5]

# k = my_list[0]
# for i in range(1, len(my_list) - 1):
#     if k <= my_list[i]:
#         k = my_list[i]
#     else:
#         print(my_list[i])
#         break


"""4-masala"""

my_list = [
    "Noilaxon",
    "noilaxonnematjonova@gmail.com",
    19,
    True,
    "bonuahadova1234@gmail.com",
]

gmail_list = []
for i in my_list:
    if isinstance(i, str):
        if "@gmail.com" in i:
            gmail_list.append(i)

print("gmaillar: ", gmail_list)
