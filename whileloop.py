# Simple while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with user input
user_input = ""
while user_input != "quit":
    user_input = input("Enter a command (or 'quit' to exit): ")
    print(f"You entered: {user_input}")

# While loop with break
number = 0
while True:
    number += 1
    if number == 10:
        break
    print(number)

# While loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)