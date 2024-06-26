""" Explaining python functions """

# Defining a function:
def hello(name):
    print("Hello, " + name)

# Calling a function:
hello("Alice")

# Return values:
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Default parameters:
def greet(name, message="Hello"):
    print(message + ", " + name)

greet("Bob")  # Uses default message
greet("Bob", "Hi")  # Custom message

# Keyword arguments:
def greet1(name, message):
    print(message + ", " + name)

greet1(message="Good morning", name="Charlie")

# Arbitrary arguments (*args):
def greet2(*names):
    for name in names:
        print("Hello, " + name)

greet2("Dave", "Eve", "Frank")

# Arbitrary keyword arguments (**kwargs):
def greet3(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)

greet3(name="Grace", message="Welcome")

# Lambda functions: Small anonymous functions.
add = lambda x, y: x + y
print(add(2, 3))  # 5

# Functions within functions:
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from the inner function!")

# Recursion: Function calling itself.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120