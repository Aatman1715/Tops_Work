# Demo of Relational and Conditional Operators in Python

# ===== RELATIONAL OPERATORS =====
print("=== RELATIONAL OPERATORS ===\n")

a = 10
b = 20

# Equal to (==)
print(f"{a} == {b}: {a == b}")

# Not equal to (!=)
print(f"{a} != {b}: {a != b}")

# Greater than (>)
print(f"{a} > {b}: {a > b}")

# Less than (<)
print(f"{a} < {b}: {a < b}")

# Greater than or equal to (>=)
print(f"{a} >= {b}: {a >= b}")

# Less than or equal to (<=)
print(f"{a} <= {b}: {a <= b}")

# ===== CONDITIONAL OPERATORS =====
print("\n=== CONDITIONAL OPERATORS ===\n")

x = 15

# if-else
if x > 10:
    print(f"{x} is greater than 10")
else:
    print(f"{x} is not greater than 10")

# if-elif-else
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Ternary operator (conditional expression)
age = 18
status = "Adult" if age >= 18 else "Minor"
print(f"\nAge {age}: {status}")

# ===== LOGICAL OPERATORS =====
print("\n=== LOGICAL OPERATORS (used with conditionals) ===\n")

p, q = True, False

# and
print(f"True and False: {p and q}")

# or
print(f"True or False: {p or q}")

# not
print(f"not True: {not p}")

# Combined example
num = 25
if num > 0 and num < 100:
    print(f"{num} is between 0 and 100")