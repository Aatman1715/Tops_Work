# name = input("Enter your name: ")
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())

#String function for endswith()
# email = input("Enter your email address: ")
# print(email.endswith("@gmail.com"))
# if email.endswith("@gmail.com"):
#     print("Valid email address")
# else:
#     print("Invalid email address")

#Program to check if a string starts with a specific number using startswith() and len() functions
# phone_number = input("Enter your phone number: ")
# if phone_number.startswith("9") and len(phone_number) == 10:
#     print("Valid phone number")
# else:
#     print("Invalid phone number")

#String count() function
# text = input("Enter a string: ")
# character = input("Enter a character to count: ")
# count = text.count(character)
# print(f"The character '{character}' appears {count} times in the string.")

#String function using count and split to find a letter from a word in a strimg
word = input("Enter a word: ")
letter = input("Enter a letter to count: ")
count = word.count(letter)
print(f"The letter '{letter}' appears {count} times in the word '{word}'.")

#Program to find the length of each word in a string
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(f"The length of the word '{word}' is {len(word)}.")

#Program to use count() function parameters
text = input("Enter a string: ")
substring = input("Enter a substring to count: ")
start_index = int(input("Enter the starting index (optional, press Enter to skip): ")or 0)
end_index = int(input("Enter the ending index (optional, press Enter to skip): ")or len(text))
count = text.count(substring, start_index, end_index)
print(f"The substring '{substring}' appears {count} times in the string between index {start_index} and {end_index}.")

#Program to use maxsplit parameter in split() function
sentence = input("Enter a sentence: ")
max_splits = int(input("Enter the maximum number of splits (optional, press Enter to skip): ")or -1)
words = sentence.split(maxsplit=max_splits)
print(f"The words in the sentence are: {words}")