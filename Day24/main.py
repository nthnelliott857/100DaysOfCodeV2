# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="r") as file:
#     content = file.read()
#     print(content)
    # default mode for 'open' is "r" or 'read only' mode
    # so we have to set it to "w" or 'write' to write to it
    # 'a' stands for 'append', a mode which we can use to add to what's already in the
    # file rather than replace it
    #file.write("my nizzle")

#with open(r'C:/Users/nthne/OneDrive/Desktop/new_file.txt', mode="r") as file: # absolute path
with open(r'..\..\..\..\..\Desktop\new_file.txt', mode="r") as file: #relative path
    # '..\' indicates to go up one level
    print(file.read())
# file = open("my_file.txt", mode="r")
# contents = file.read()
# print(contents)
# file.close()
#
# file = open("my_file.txt", mode="w")
# file.write("shrek")
# file.close()
#
# file = open("my_file.txt", mode="r")
# contents1 = file.read()
# print(contents1)
# file.close()