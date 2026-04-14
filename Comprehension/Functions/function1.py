#Simple python function to greet a person by their name
# def greet(name):
#     return f"Hello, {name}! Welcome to Python programming."
# user_name = input("Please enter your name: ")
# greeting_message = greet(user_name)
# print(greeting_message)

#Function to store student details like Name, Roll_No and age of the student and print the details 
#taking value from user.
def student_details(name, roll_no, age):
    return f"Name: {name}, Roll No: {roll_no}, Age: {age}"  
name = input("Enter the student's name: ")
roll_no = input("Enter the student's roll number: ")
age = input("Enter the student's age: ")
details = student_details(name, roll_no, age)
print(details)
