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
rows = int(input("Enter the number of rows: "))  
for num in range(rows+1):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for i in range(num):  
            print(num, end=" ")       
  
        #End line after each row  
        print()