count = 1
while count < 5:
    print(count)
    count += 1

text = "Hello"
index = 0
while index < len(text):
    print(text[index])
    index += 1

grades = {"saira": 92, "ali": 79, "Ahmad": 98}
keys = list(grades.keys())
index = 0
while index < len(keys):
    key = keys[index]
    value = grades[key]
    print(f"{key}: {value}")
    index += 1
