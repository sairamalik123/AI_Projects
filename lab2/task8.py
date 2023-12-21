numbers = [10, 20, 30, 40, 50]

for number in numbers:
    result = number * 2
    print(result)

text = "Hello World"

for char in text:
    print(char)

newText = ""

for char in text:
    if char.isalpha():
        newText += char.upper()
    else:
        newText += char

print(newText)

numericData = []

for i in range(1, 11):
    numericData.append(i)

print(numericData)