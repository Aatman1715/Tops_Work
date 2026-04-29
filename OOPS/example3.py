#Code to create a employee class with attributes like ID, name, department, and salary. The class should have a method to display the details of the employee, and take multiple inputs as a list from the user to create objects of the employee class and display its details.
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Employee Details:")
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
employees = []
num_employees = int(input("Enter the number of employees you want to add: "))
for _ in range(num_employees):  
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")
    employee = Employee(emp_id, name, department, salary)
    employees.append(employee)
for employee in employees:
    employee.display_details()
    print()

#find employee for software department, earns more than 10000 and 
#the code should be menu driven to find employee details based on user input and also update, delete and search employee details based on user input.
def find_employees_by_department_and_salary(department, salary_threshold):
    found_employees = []
    for employee in employees:
        if employee.department == department and int(employee.salary) > salary_threshold:
            found_employees.append(employee)
    return found_employees
def update_employee(emp_id, name=None, department=None, salary=None):
    for employee in employees:
        if employee.emp_id == emp_id:
            if name:
                employee.name = name
            if department:
                employee.department = department
            if salary:
                employee.salary = salary
            return True
    return False
def delete_employee(emp_id):
    global employees
    employees = [employee for employee in employees if employee.emp_id != emp_id]
def search_employee(emp_id):
    for employee in employees:
        if employee.emp_id == emp_id:
            return employee
    return None
while True:
    print("Menu:")
    print("1. Find Employees by Department and Salary")
    print("2. Update Employee Details")
    print("3. Delete Employee")
    print("4. Search Employee")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        dept = input("Enter Department: ")
        salary_threshold = int(input("Enter Salary Threshold: "))
        found_employees = find_employees_by_department_and_salary(dept, salary_threshold)
        for emp in found_employees:
            emp.display_details()
            print()
    
    elif choice == '2':
        emp_id = input("Enter Employee ID to update: ")
        name = input("Enter new Name (leave blank to keep unchanged): ")
        department = input("Enter new Department (leave blank to keep unchanged): ")
        salary = input("Enter new Salary (leave blank to keep unchanged): ")
        if update_employee(emp_id, name, department, salary):
            print("Employee updated successfully.")
        else:
            print("Employee not found.")
    
    elif choice == '3':
        emp_id = input("Enter Employee ID to delete: ")
        delete_employee(emp_id)
        print("Employee deleted successfully.")
    
    elif choice == '4':
        emp_id = input("Enter Employee ID to search: ")
        employee = search_employee(emp_id)
        if employee:
            employee.display_details()
            print()
        else:
            print("Employee not found.")
    
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")  