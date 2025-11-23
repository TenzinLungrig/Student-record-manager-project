# Student Record Manager
# By Tenzin Lungrig

students = []

def add_student():
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    students.append({"name": name, "roll": roll, "marks": marks})
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No records found!\n")
    else:
        print("\n--- Student Records ---")
        for s in students:
            print(f"Name: {s['name']}, Roll No: {s['roll']}, Marks: {s['marks']}")
        print()

def search_student():
    roll = int(input("Enter roll number to search: "))
    for s in students:
        if s["roll"] == roll:
            print(f"Record Found - Name: {s['name']}, Marks: {s['marks']}\n")
            return
    print("Student not found!\n")

def sort_students():
    # Bubble Sort based on marks
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j]["marks"] > students[j + 1]["marks"]:
                students[j], students[j + 1] = students[j + 1], students[j]
    print("Records sorted by marks successfully!\n")

while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Roll No")
    print("4. Sort Students by Marks")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        sort_students()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
