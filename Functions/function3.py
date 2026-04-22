#1. ⁠Create a function that counts how many times a character appears in a string.
def count_character(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count
input_string = input("Enter a string: ")
input_character = input("Enter a character to count: ")
result = count_character(input_string, input_character)
print(f"The character '{input_character}' appears {result} times in the string.")
#2.⁠ ⁠Write a function to find the smallest number in a list.
def find_smallest_number(numbers):
    if not numbers:
        return "The list is empty."
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
input_list = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(float, input_list.split()))
smallest_number = find_smallest_number(numbers)
print(f"The smallest number in the list is: {smallest_number}")

# 3.⁠ ⁠Write a function that formats a phone number (e.g., "9876543210" → "98765-43210").
def format_phone_number(phone_number):
    if len(phone_number) != 10 or not phone_number.isdigit():
        return "Invalid phone number. Please enter a 10-digit number."
    return f"{phone_number[:5]}-{phone_number[5:]}"
input_phone_number = input("Enter a 10-digit phone number: ")
formatted_number = format_phone_number(input_phone_number)
print(f"Formatted phone number: {formatted_number}")
# 4.⁠ ⁠Write a function that calculates the total price after adding 18% GST.
def calculate_total_price(price):
    gst = price * 0.18
    total_price = price + gst
    return total_price
input_price = float(input("Enter the price: "))
total_price = calculate_total_price(input_price)
print(f"The total price after adding 18% GST is: {total_price}")
# 5.⁠ ⁠Write a function that sorts a list without using built-in sort() or sorted().
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
input_list = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(float, input_list.split()))
sorted_numbers = bubble_sort(numbers)
print(f"Sorted list: {sorted_numbers}")
# 6.⁠ ⁠Create a function that validates a password:At least 8 characters,Contains uppercase, lowercase, and numbers.
def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number."
    return "Password is valid."
input_password = input("Enter a password to validate: ")
validation_result = validate_password(input_password)
print(validation_result)

#Function with keyword arguments (with 2 stars)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Alice", age=30, city="New York")
#Function with variable-length arguments
def sum_numbers(*args):
    total = sum(args)
    return f"The sum of the numbers is: {total}"
result = sum_numbers(1, 2, 3, 4, 5)
print(result)
