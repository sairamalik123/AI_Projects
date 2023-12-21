x = 2
y = 10

if x > 2:
    print("x > 2")
elif x == 2 and y > 50:
    print("x == 2 and y > 50")
elif x < 10 or y > 50:
    print("x < 10 or y > 50")
else:
    print("Nothing happened")

nameList1 = ["John", "Jill"]
nameList2 = ["John", "Jill"]

print(not (nameList1 == nameList2))

print(nameList1 == nameList2)
print(nameList1 is nameList2)