#Code -1: Write a program to display the sum of the firt n positive integers.
n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("The sum of the first", n, "positive integers is:", sum)

#Code -2: Write a program to count occurrences of a substring in a given string.
string = input("Enter a string: ")
substring = input("Enter a substring to count: ")
count = string.count(substring)
print("The substring", substring, "occurs", count, "times in the string.")

#Code -3: Write a program to count the occurences of each word in a given string.
string = input("Enter a string: ")
words = string.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word occurrences:")
for word, count in word_count.items():
    print(word + ":", count)

#Code -4: Write a program ti get a single String from two given strings, separated by a space and swap the first two characters of each string.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if len(string1) < 2 or len(string2) < 2:
    print("Both strings must have at least 2 characters.")
else:
    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2] + string2[2:]
    result = new_string1 + " " + new_string2
    print("The resulting string is:", result)

#Code -5: Write a Python program to add 'ing' at the end of a given string (length should be at least 3).If the given string already ends with 'ing' then add 'ly' instead If the string length of the given string is less than 3, leave it unchanged.
string = input("Enter a string: ")
if len(string) < 3:
    print("The string is unchanged:", string)
elif string.endswith("ing"):
    new_string = string + "ly"
    print("The modified string is:", new_string)
else:
    new_string = string + "ing"
    print("The modified string is:", new_string)

#Code -6: Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.Return the resulting string.
string = input("Enter a string: ")
poor_index = string.find("poor")
not_index = string.find("not")

if poor_index != -1 and not_index != -1 and poor_index < not_index:
    result = string[:poor_index] + "good" + string[not_index + 3:]
    print("The resulting string is:", result)
else:
    print("The resulting string is:", string)

#Code -7: Write a program to find the GCD of two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", result)

#Code -8: Write a program to check whether a list contains a sublist.
main_list = input("Enter the main list (comma separated): ").split(",")
sublist = input("Enter the sublist (comma separated): ").split(",")
if all(item in main_list for item in sublist):
    print("The main list contains the sublist.")
else:
    print("The main list does not contain the sublist.")

#Code -9: Write a program to find the second smallest number in a list.
numbers = list(map(int, input("Enter a list of numbers (comma separated): ").
split(",")))
unique_numbers = list(set(numbers))
if len(unique_numbers) < 2:
    print("There is no second smallest number.")
else:
    unique_numbers.sort()
    second_smallest = unique_numbers[1]
    print("The second smallest number is:", second_smallest)

#Code -10: Write a program to get unique values from a list.
numbers = list(map(float, input("Enter a list of numbers (comma separated): ").split(",")))
unique_numbers = list(set(numbers))
print("Unique values from the list:", unique_numbers)
