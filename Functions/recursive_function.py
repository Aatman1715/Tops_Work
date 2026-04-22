#Code to understand the concept of recursion in Python.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# number = int(input("Enter a number to find its factorial: "))
# result = factorial(number)
# print(f"The factorial of {number} is {result}")

#Code to understand the concept of generator in Python.
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = list(fibonacci_generator(n))
print(f"The first {n} Fibonacci numbers are: {fib_sequence}")