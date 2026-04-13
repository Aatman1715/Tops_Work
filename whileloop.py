# # Simple while loop
# count = 0
# while count < 5:
#     print(f"Count: {count}")
#     count += 1

# # While loop with user input
# user_input = ""
# while user_input != "quit":
#     user_input = input("Enter a command (or 'quit' to exit): ")
#     print(f"You entered: {user_input}")

# # While loop with break
# number = 0
# while True:
#     number += 1
#     if number == 10:
#         break
#     print(number)

# # While loop with continue
# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

#Factorial using while loop
# num = int(input("Enter a number: "))
# factorial = 1
# while num > 1:
#     factorial *= num
#     num -= 1
# print(f"Factorial is {factorial}")

#Number is prime or not using while loop
# num = int(input("Enter a number: "))
# if num > 1:
#     i = 2
#     while i <= int(num**0.5):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#         i += 1
#     else:
#         print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

#Count the number of digits in a number using while loop
# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     num //= 10
#     print(f"Current number: {num}, Count: {count}")
#     count += 1
# print(f"The number of digits is: {count}")

#Sum of the digits in a number using while loop
# num = int(input("Enter a number: "))
# total_sum = 0
# while num > 0:
#     digit = num % 10
#     total_sum += digit
#     num //= 10
# print(f"The sum of the digits is: {total_sum}")

#Count total even numbers and odd numbers in the given numbers using while loop
# num = int(input("Enter a number: "))
# even_count = 0
# odd_count = 0
# while num > 0:
#     digit = num % 10
#     if digit % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#     num //= 10
# print(f"Total even numbers: {even_count}")
# print(f"Total odd numbers: {odd_count}")

#Armstrong number check using while loop
# num = int(input("Enter a number: "))
# order = len(str(num))
# sum_of_digits = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum_of_digits += digit ** order
#     temp //= 10
# if num == sum_of_digits:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")

#Fibonacci series like a pyramid up to n using while loop
n = int(input("Enter a positive integer: "))
fib_series = []
a, b = 0, 1
while a <= n:
    fib_series.append(a)
    a, b = b, a + b
print("Fibonacci series up to", n, ":", fib_series)