""" Explaining python user input & arguments """

# User Input: Taking input from the user.

# Basic input:
name = input("Enter your name: ")
print("Hello, " + name)

# Input with a prompt:
age = input("Enter your age: ")
print("You are " + age + " years old")

# Converting input to integers/floats:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The sum is:", num1 + num2)

# Handling invalid input:
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")

# Using input in a loop:
while True:
    data = input("Enter something (type 'exit' to quit): ")
    if data.lower() == 'exit':
        break
    print("You entered:", data)


# Python Script Arguments: Using arguments passed to a script from the command line.

import sys

# Accessing arguments:
args = sys.argv  # List of command line arguments
print("Arguments passed to the script:", args)

# Example: Running script with arguments
# Command: python script.py arg1 arg2
# Output:
# Arguments passed to the script: ['script.py', 'arg1', 'arg2']

# Handling arguments:
if len(args) > 1:
    print("First argument:", args[1])
    if len(args) > 2:
        print("Second argument:", args[2])

# Using argparse for more complex argument parsing:
import argparse

# Creating the parser:
parser = argparse.ArgumentParser(description="A script that processes arguments.")

# Adding arguments:
parser.add_argument("name", type=str, help="Name of the user")
parser.add_argument("--age", type=int, help="Age of the user", default=25)
parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

# Parsing arguments:
parsed_args = parser.parse_args()

# Using parsed arguments:
print("Hello, " + parsed_args.name)
print("You are " + str(parsed_args.age) + " years old")

if parsed_args.verbose:
    print("Verbose mode is enabled")

# Example: Running script with argparse
# Command: python script.py John --age 30 --verbose
# Output:
# Hello, John
# You are 30 years old
# Verbose mode is enabled
