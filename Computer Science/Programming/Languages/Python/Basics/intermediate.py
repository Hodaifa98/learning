""" Explaining python concepts """

# Iterators, Scope, Datetime.

# Iterators: Objects that can be iterated upon (implements __iter__ and __next__ methods).

# Creating an iterator from a list:
fruits = ["apple", "banana", "cherry"]
fruit_iter = iter(fruits)
print(next(fruit_iter))  # apple
print(next(fruit_iter))  # banana
print(next(fruit_iter))  # cherry

# Custom iterator:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))  # 1
print(next(myiter))  # 2

# Scope: The region where a variable is recognized.

# Local scope:
def my_function():
    x = 300  # Local variable
    print(x)

my_function()
# print(x)  # Error: x is not defined

# Global scope:
y = 200  # Global variable

def another_function():
    print(y)  # Can access global variable

another_function()

# Global keyword:
def yet_another_function():
    global z
    z = 100

yet_another_function()
print(z)  # 100

# Dates: Working with dates and times.

import datetime

# Current date and time:
now = datetime.datetime.now()
print(now)  # e.g., 2024-06-26 10:53:32.123456

# Creating a specific date:
my_birthday = datetime.datetime(1990, 5, 17)
print(my_birthday)  # 1990-05-17 00:00:00

# Formatting dates:
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # e.g., 2024-06-26 10:53:32

# Parsing dates from strings:
date_string = "2024-06-26 10:53:32"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)  # 2024-06-26 10:53:32

# Date arithmetic:
tomorrow = now + datetime.timedelta(days=1)
print(tomorrow)  # e.g., 2024-06-27 10:53:32.123456

# Difference between dates:
date_diff = now - my_birthday
print(date_diff.days)  # Number of days between now and my birthday
