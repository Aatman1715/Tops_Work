#Simple * pyramid pattern using for loop
# rows = int(input("Enter the number of rows: "))
# for i in range(0, rows):  
#     #Inner for loop to handle number of columns  
#     #values change according to the outer loop  
#         for j in range(0, i + 1):  
#             print("* ", end=" ")       
#         #End line after each row  
#         print()

#Simple alphabet pyramid pattern using for loop
# rows = int(input("Enter the number of rows: "))  
# for num in range(rows+1):  
#     #Inner for loop to handle number of columns  
#     #values change according to the outer loop  
#         for i in range(num):  
#             print(num, end=" ")       
  
#         #End line after each row  
#         print()

#Factorial using for loop
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"Factorial of {num} is {factorial}")

#Sum of n numbers using for loop
n = int(input("Enter a positive integer: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"The sum of the first {n} natural numbers is: {total_sum}")
