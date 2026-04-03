#Simple * pyramid pattern using for loop
# rows = int(input("Enter the number of rows: "))
# for i in range(0, rows):  
#         for j in range(0, i + 1):  
#             print("* ", end=" ")         
#         print()

#Pattern to print odd numbers in a pyramid shape using for loop
# rows = int(input("Enter the number of rows: "))
# num = 1
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print(num, end=" ")
#         num += 2
#     print()

#Pattern to print alphabets in a pyramid shape using for loop
#Output:
# A
# A B
# A B C
# rows = int(input("Enter the number of rows: "))
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print(chr(65 + j), end=" ")
#     print()

#Pattern for half diamond using for loop
#Output:
# * * * *
# * * *
# * *
# *
# *
# * * 
# * * * 
# * * * *

rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end="")
    print()
for i in range(1, rows + 1):
    for j in range(0, i):
        print("* ", end="")
    print()


#Simple alphabet pyramid pattern using for loop
# rows = int(input("Enter the number of rows: "))  
# for num in range(rows+1):  
#         for i in range(num):  
#             print(num, end=" ")        
#         print()

#Factorial using for loop
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"Factorial of {num} is {factorial}")

#Sum of n numbers using for loop
# n = int(input("Enter a positive integer: "))
# total_sum = 0
# for i in range(1, n + 1):
#     total_sum += i
# print(f"The sum of the first {n} natural numbers is: {total_sum}")

#Number is prime or not using for loop
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

#Count the number of digits in a number using for loop
# num = int(input("Enter a number: "))
# count = 0
# for digit in str(num):
#     count += 1
# print(f"The number of digits is: {count}")