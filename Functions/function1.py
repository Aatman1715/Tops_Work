#Simple python function to greet a person by their name
# def greet(name):
#     return f"Hello, {name}! Welcome to Python programming."
# user_name = input("Please enter your name: ")
# greeting_message = greet(user_name)
# print(greeting_message)

#Function to store student details like Name, Roll_No and age of the student and print the details 
#taking value from user.
# def student_details(name, roll_no, age):
#     return f"Name: {name}, Roll No: {roll_no}, Age: {age}"  
# name = input("Enter the student's name: ")
# roll_no = input("Enter the student's roll number: ")
# age = input("Enter the student's age: ")
# details = student_details(name, roll_no, age)
# print(details)

#Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."
num = int(input("Enter a number: "))
result = check_even_odd(num)
print(result) 

#1. Function which prints the number is positive or negative or zero
def check_positive_negative_zero(number):
    if number > 0:
        return f"{number} is a positive number."
    elif number < 0:
        return f"{number} is a negative number."
    else:
        return f"{number} is zero."
num = float(input("Enter a number: "))
result = check_positive_negative_zero(num)
print(result)
#2. Function which prints the number is prime or not.
def is_prime(number):
    if number <= 1:
        return f"{number} is not a prime number."
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return f"{number} is not a prime number."
    return f"{number} is a prime number."
num = int(input("Enter a number: "))
result = is_prime(num)
print(result)
#3. Function which prints square of a given number.
def square(number):
    return f"The square of {number} is {number ** 2}."
num = float(input("Enter a number: "))
result = square(num)
print(result)