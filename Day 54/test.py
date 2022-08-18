
list2 = [1, 2, 3, 4, 5, 6, 7]
# print(list2)
# list2.pop(0)
# print(list2)

# for i in range(1, int(len(list2)/2), 2):
#     print(list2[i + 1])



for i in range(1, int(len(list2)/2) + 1, 1):
    print(list2)
    list2.pop(i)
    print(list2)
