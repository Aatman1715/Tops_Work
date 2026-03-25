# # Code 1: Relational Operators
# print("=== Relational Operators ===")

# a = 10
# b = 20

# print(f"a = {a}, b = {b}")
# print(f"a == b: {a == b}")  # Equal to
# print(f"a != b: {a != b}")  # Not equal to
# print(f"a < b: {a < b}")    # Less than
# print(f"a > b: {a > b}")    # Greater than
# print(f"a <= b: {a <= b}")  # Less than or equal to
# print(f"a >= b: {a >= b}")  # Greater than or equal to

# # Code 2: Logical Operators

# print("\n=== Logical Operators ===")

# x = 5
# y = 15
# z = 25

# print(f"x = {x}, y = {y}, z = {z}")
# print(f"x < y and y < z: {x < y and y < z}")           # AND
# print(f"x > y or y < z: {x > y or y < z}")             # OR
# print(f"not (x > y): {not (x > y)}")                   # NOT
# print(f"(x < y) and (z > y) and (x != z): {(x < y) and (z > y) and (x != z)}")
# print(f"(x > 10) or (y == 15): {(x > 10) or (y == 15)}")

#Code 3 : Print that the number is positive or negative

print("\n=== Check if a number is positive or negative ===")
number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")