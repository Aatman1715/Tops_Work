# Program to demonstrate if-elif statements with user input

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")