<<<<<<< HEAD
#Python code to study the comprehensive of python
#List comprehension
squares = [x**2 for x in range(10)]
print(squares)
=======
# # Basic list comprehension
# squares = [x**2 for x in range(10)]
# print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# # With condition
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)  # [0, 2, 4, 6, 8]
# # With transformation
# words = ["hello", "world", "python"]
# upper_words = [word.upper() for word in words]
# print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']
# # Nested list comprehension
# matrix = [[i*j for j in range(3)] for i in range(3)]
# print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
# # From existing list
# numbers = [1, 2, 3, 4, 5]
# doubled = [num * 2 for num in numbers]
# print(doubled)  # [2, 4, 6, 8, 10]
# # Multiple conditions
# filtered = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
# print(filtered)  # [0, 6, 12, 18]

#Check if the list is even or odd
# numbers = [1, 2, 3, 4, 5, 6]
# parity = ["even" if num % 2 == 0 else "odd" for num in numbers]
# print(parity)

# #Comprehension with dictionary
# squared_dict = {x: x**2 for x in range(5)}
# print(squared_dict)

#List of cities print dict having city name with
#number of letters using dict comprehension
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]
city_length = {city: len(city) for city in cities}
print(city_length)

>>>>>>> c60a68d2055c9b500b22ce016183e7b97e394450
