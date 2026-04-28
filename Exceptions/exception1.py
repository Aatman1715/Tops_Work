#Code to manage various exceptions in Python
try:   
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:    # Handling division by zero error
    print("Error: You cannot divide by zero.")
except ValueError:    # Handling invalid input error
    print("Error: Please enter valid integers.")
except Exception as e:    # Handling any other exceptions
    print(f"An unexpected error occurred: {e}") 
finally:    # Code that will always execute
    print("Execution completed.")

#Code to handle file handling exceptions
try:
    file = open("non_existent_file.txt", "r")  # Attempting to open a non-existent file
    content = file.read()
    print(content)
except FileNotFoundError:    # Handling file not found error
    print("Error: The file you are trying to open does not exist.")
except Exception as e:    # Handling any other exceptions
    print(f"An unexpected error occurred: {e}")
finally:    # Code that will always execute
    print("File handling execution completed.")