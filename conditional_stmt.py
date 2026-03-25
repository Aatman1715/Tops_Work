# Program to demonstrate if-elif statements with user input

# age = int(input("Enter your age: "))

# if age < 13:
#     print("You are a child.")
# elif age < 18:
#     print("You are a teenager.")
# elif age < 60:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

# Code to check the grade of a student based on their marks where the grading system is as follows:
# 90-100: A
# 80-89: B
# 70-79: C  
# 60-69: D
# Below 60: F
marks = float(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Your grade is: A")
elif marks >= 80 and marks < 90:
    print("Your grade is: B")
elif marks >= 70 and marks < 80:
    print("Your grade is: C")
elif marks >= 60 and marks < 70:
    print("Your grade is: D")
elif marks >= 0 and marks < 60:
    print("Your grade is: F")
else:
    print("Invalid marks entered. Please enter a value between 0 and 100.")

