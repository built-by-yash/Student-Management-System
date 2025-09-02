students = {}
def add_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    subjects = input("Enter subjects (comma separated): ").split(",")
    marks = list(map(int, input("Enter marks (comma separated): ").split(",")))
    clubs = set(input("Enter clubs (comma separated): ").split(","))
    
    students[sid] = {
        "info": (sid, name),
        "subjects": subjects,
        "marks": marks,
        "clubs": clubs
    }
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    for sid, data in students.items():
        print(f"ID: {sid}, Name: {data['info'][1]}")
        print(f" Subjects: {data['subjects']}")
        print(f"Marks: {data['marks']}")
        print(f"Clubs:{data['clubs']}\n")

    else:
        print("Student not found.\n")   

def search_student():
    sid = int(input("Enter Student ID to search: "))
    if sid in students:
        data = students[sid]
        print(f"ID: {sid}, Name: {data['info'][1]}")
        print(f" Subjects: {data['subjects']}")
        print(f" Marks: {data['marks']}")
        print(f" Clubs: {data['clubs']}\n")
    
    else:
        print(" Student not found.\n")

def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    if sid in students:
        del students[sid]
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.\n")



