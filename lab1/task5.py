myList = []
myList.append(1)
myList.append(2)
myList.append(3)

print(myList[-1])

names = ["saira", 1, "ahmad", 2, "ali", 3, "abdullah", 4]
print("Number of names in list: {}".format(len(names)))

new_list = []

for x in names:
    if isinstance(x, str):
        new_list.append(x)
print("updated List with number of only names in list:{}".format(len(new_list)))

for x in new_list:
    print("{}".format(x))


