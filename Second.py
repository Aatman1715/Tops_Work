#Code to take input from the user and display it back to them

# name = input("What is your name? ")
# age = int(input("What is your age? "))
# address = input("What is your address? ")

# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Address: {address}")


#20th March, 2026

#1 - Code to understand arithmetic operators

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# sum = num1 + num2
# subtract = num1 - num2
# multiply = num1 * num2
# divide = num1 / num2
# remainder = num1 % num2
# exponent = num1 ** num2
# floor_division = num1 // num2
# print(f"The sum of {num1} and {num2} is: {sum}")
# print(f"The difference of {num1} and {num2} is: {subtract}")
# print(f"The product of {num1} and {num2} is : {multiply}")
# print(f"The quotient of {num1} and {num2} is: {divide}")
# print(f"The remainder of {num1} and {num2} is: {remainder}")
# print(f"The exponent of {num1} and {num2} is: {exponent}")
# print(f"The floor division of {num1} and {num2} is: {num1 // num2}")

#2 - Code to find area of circle

# radius = float(input("Enter the radius of the circle: "))
# pi = 3.14159
# area = pi * radius ** 2
# print(f"The area of the circle with radius {radius} is: {area}")

#3 - Code to find maximum of two numbers using max function

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# maximum = max(num1, num2)
# print(f"The maximum of {num1} and {num2} is: {maximum}")

#4 - Code to find maximum of two numbers using ternary operator

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# maximum = num1 if num1 > num2 else num2
# print(f"The maximum of {num1} and {num2} is: {maximum}")

#5 - Code to find Simple Interest

# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest: "))
# time = float(input("Enter the time in years: "))
# simple_interest = (principal * rate * time) / 100
# print(f"The simple interest is: {simple_interest}")

#6 - Code to find Compound Interest

# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest: "))
# time = float(input("Enter the time in years: "))
# compound_interest = principal * (1 + rate / 100) ** time - principal
# print(f"The compound interest is: {compound_interest}")

#7- Code to print ASCII value to letter

# ascii_value = int(input("Enter an ASCII value: "))
# character = chr(ascii_value)
# print(f"The character corresponding to ASCII value {ascii_value} is: {character}")

#8 - Code to convert Farenhit to Celsius and vice versa

# choice = input("Do you want to convert Farenhit to Celsius (F to C) or Celsius to Farenhit (C to F)? ")
# if choice == "F to C":
#     farenhit = float(input("Enter the temperature in Farenhit: "))
#     celsius = (farenhit - 32) * 5 / 9
#     print(f"{farenhit} Farenhit is equal to {celsius} Celsius.")
# elif choice == "C to F":
#     celsius = float(input("Enter the temperature in Celsius: "))
#     farenhit = (celsius * 9 / 5) + 32
#     print(f"{celsius} Celsius is equal to {farenhit} Farenhit.")
# else:
#     print("Invalid choice. Please choose either 'F to C' or 'C to F'.")

#9 - Code to print multiplication table of a number

number = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")