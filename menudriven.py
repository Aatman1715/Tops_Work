#Create a menu driven program to perform factorial, count of digits,
# sum of digits, prime number check and exit uising while loop.
while True:
    print("\nMenu:")
    print("1. Factorial")
    print("2. Count of digits")
    print("3. Sum of digits")
    print("4. Prime number check")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            num = int(input("Enter a number: "))
            factorial = 1
            while num > 1:
                factorial *= num
                num -= 1
            print(f"Factorial is {factorial}")
        case 2:
            num = int(input("Enter a number: "))
            count = 0
            while num > 0:
                num //= 10
                count += 1
            print(f"The number of digits is: {count}")
        case 3:
            num = int(input("Enter a number: "))
            total_sum = 0
            while num > 0:
                total_sum += num % 10
                num //= 10
            print(f"The sum of the digits is: {total_sum}")
        case 4:
            num = int(input("Enter a number: "))
            if num > 1:
                i = 2
                while i <= int(num**0.5):
                    if num % i == 0:
                        print(f"{num} is not a prime number.")
                        break
                    i += 1
                else:
                    print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        case 5:
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")
