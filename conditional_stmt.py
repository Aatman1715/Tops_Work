# Code to check the age of a person and determine if they are a child, teenager, adult, or senior citizen and the age should be taken as input from the user.between 0 and 100.
age = int(input("Enter your age: "))
if age >= 0 and age <= 12:
    print("You are a child.")
elif age > 12 and age <= 19:
    print("You are a teenager.")
elif age > 19 and age <= 59:
    print("You are an adult.")
elif age >= 60 and age <= 100:
    print("You are a senior citizen.")
else:
    print("Invalid age entered. Please enter a value between 0 and 100.")


# Code to check the grade of a student based on their marks where the grading system is as follows:
# 90-100: A
# 80-89: B
# 70-79: C  
# 60-69: D
# Below 60: F
# marks = float(input("Enter your marks: "))
# if marks >= 90 and marks <= 100:
#     print("Your grade is: A")
# elif marks >= 80 and marks < 90:
#     print("Your grade is: B")
# elif marks >= 70 and marks < 80:
#     print("Your grade is: C")
# elif marks >= 60 and marks < 70:
#     print("Your grade is: D")
# elif marks >= 0 and marks < 60:
#     print("Your grade is: F")
# else:
#     print("Invalid marks entered. Please enter a value between 0 and 100.")

