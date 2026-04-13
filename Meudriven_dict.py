#Menu driven program using dictionary for adding, deleting, and displaying and searching employees.
employees = {}
def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    employees[emp_id] = name
    print("Employee added successfully.")
def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully.")
    else:
        print("Employee ID not found.")
def display_employees():
    if employees:
        print("Employee List:")
        for emp_id, name in employees.items():
            print(f"ID: {emp_id}, Name: {name}")
    else:
        print("No employees to display.")
def search_employee():
    emp_id = input("Enter employee ID to search: ")
    if emp_id in employees:
        print(f"Employee found: ID: {emp_id}, Name: {employees[emp_id]}")
    else:
        print("Employee ID not found.")
while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Display Employees")
    print("4. Search Employee")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_employee()
    elif choice == '2':
        delete_employee()
    elif choice == '3':
        display_employees()
    elif choice == '4':
        search_employee()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")