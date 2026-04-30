# Design a Python class SchoolManagement that helps manage student admissions and
# records. The system should support:
# New Admission:
# Collect student name, age, class (1–12), and guardian's mobile number.
# Assign a unique student ID automatically.
# Validate age: must be between 5 and 18.
# Validate mobile number: must be 10 digits.
# View Student Details:
# Allow lookup using student ID.
# Update Student Info:
# Update mobile number or class.
# Remove Student Record:
# Remove a student using their student ID.
# Exit System
class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.next_id = 1

    def new_admission(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        student_class = int(input("Enter student class (1-12): "))
        guardian_mobile = input("Enter guardian's mobile number: ")

        if age < 5 or age > 18:
            print("Invalid age. Age must be between 5 and 18.")
            return
        
        if len(guardian_mobile) != 10 or not guardian_mobile.isdigit():
            print("Invalid mobile number. Mobile number must be 10 digits.")
            return
        
        student_id = self.next_id
        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "guardian_mobile": guardian_mobile
        }
        self.next_id += 1
        print(f"Student admitted successfully! Student ID: {student_id}")

    def view_student_details(self):
        student_id = int(input("Enter student ID to view details: "))
        
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Student ID: {student_id}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Class: {student['class']}")
            print(f"Guardian Mobile: {student['guardian_mobile']}")
        else:
            print("Student ID not found.")

    def update_student_info(self):
        student_id = int(input("Enter student ID to update info: "))
        
        if student_id in self.students:
            choice = input("What do you want to update? (mobile/class): ")
            
            if choice == "mobile":
                new_mobile = input("Enter new mobile number: ")
                if len(new_mobile) != 10 or not new_mobile.isdigit():
                    print("Invalid mobile number. Mobile number must be 10 digits.")
                    return
                self.students[student_id]["guardian_mobile"] = new_mobile
                print("Mobile number updated successfully!")
            
            elif choice == "class":
                new_class = int(input("Enter new class (1-12): "))
                if new_class < 1 or new_class > 12:
                    print("Invalid class. Class must be between 1 and 12.")
                    return
                self.students[student_id]["class"] = new_class
                print("Class updated successfully!")
            else:
                print("Invalid choice.")
        else:
            print("Student ID not found.")
    def remove_student_record(self):
        student_id = int(input("Enter student ID to remove record: "))
        if student_id in self.students:
            del self.students[student_id]
            print("Student record removed successfully!")
        else:
            print("Student ID not found.")
school = SchoolManagement()
while True:    
    print("\n1. New Admission")
    print("2. View Student Details")
    print("3. Update Student Info")
    print("4. Remove Student Record")
    print("5. Exit System")
    choice = input("Enter your choice: ")
    if choice == "1":
        school.new_admission()
    elif choice == "2":
        school.view_student_details()
    elif choice == "3":
        school.update_student_info()
    elif choice == "4":
        school.remove_student_record()
    elif choice == "5":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")