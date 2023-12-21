student_records = {}

while True:
    print("\nOptions:")
    print("1. Create a student record")
    print("2. Read a student record")
    print("3. Update a student record")
    print("4. Delete a student record")
    print("5. Show all student records")
    print("6. Exit")
    choice = input("enter the choice which you want: ")

    if choice=="1":
        std_registration_no = input("Enter registration no: ")
        name = input("Enter student name: ")
        email = input("Enter email: ")
        gender = input("Enter gender: ")
        if std_registration_no not in student_records:
            student_records[std_registration_no]={"name": name, "email": email, "gender": gender}
            print(f"Student record for {name} (ID: {std_registration_no}) created successfully.")
        else:
            print(f"Student record with ID {std_registration_no} already exists.")
    elif choice == "2":
        std_registration_no = input("Enter student registration no to read: ")
        if std_registration_no in student_records:
            record = student_records[std_registration_no]
            print(f"Registration no: {std_registration_no}")
            print(f"Name: {record['name']}")
            print(f"Email: {record['email']}")
            print(f"Gender: {record['gender']}")
        else:
            print(f"Student record with ID {std_registration_no} not found.")
    elif choice == "3":
        std_registration_no = input("Enter student registration no to update: ")
        if std_registration_no in student_records:
            name = input("Enter new student name: ")
            email = input("Enter new student email: ")
            gender = input("Enter new student gender: ")
            student_records[std_registration_no] = {"name": name, "email": email, "gender": gender}
            print(f"Student record for registration no {std_registration_no} updated successfully.")
        else:
            print("Student record for registration number not exist")
    elif choice == "4":
        std_registration_no = input("Enter registration number to delete: ")
        if std_registration_no in student_records:
            del student_records[std_registration_no]
            print(f"Student record for registration {std_registration_no} deleted successfully.")
        else:
            print(f"Student record with registration {std_registration_no} not found.")
    elif choice=="5":
        print("\nAll Student Records:")
        for std_registration_no, record in student_records.items():
            print(f"Student ID: {std_registration_no}")
            print(f"Name: {record['name']}")
            print(f"Email: {record['email']}")
            print(f"Gender: {record['gender']}")
            print()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please choose a valid option.")