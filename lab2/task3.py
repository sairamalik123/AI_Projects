phonebook = {}
phonebook["Jhon"] = {"Phone": "0332525345", "Email": "jhon@gmail.com"}
phonebook["Jill"] = {"Phone": "0321543525", "Email": "jill@gmail.com"}
phonebook["Joss"] = {"Phone": "0333351345", "Email": "joss@gmail.com"}
print(phonebook)

for name, record in phonebook.items():
    print("{}'s phone number is {}, and email is {}".format(name, record["Phone"], record["Email"]))

jill_record = phonebook.pop("Jill")
for name, record in phonebook.items():
    print("{}'s phone number is {}, and email is {}".format(name, record["Phone"], record["Email"]))

del phonebook["Ali"]