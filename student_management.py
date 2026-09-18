students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        students[roll_no] = name
        print("Student Added Successfully")

    elif choice == 2:
        for roll_no, name in students.items():
            print(roll_no, "-", name)

    elif choice == 3:
        roll_no = input("Enter Roll Number: ")
        if roll_no in students:
            print("Student Found:", students[roll_no])
        else:
            print("Student Not Found")

    elif choice == 4:
        roll_no = input("Enter Roll Number: ")
        if roll_no in students:
            del students[roll_no]
            print("Student Deleted")
        else:
            print("Student Not Found")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
