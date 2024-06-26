""" Explaining python modules """

# Modules: Files containing Python code (functions, classes, variables).

# Importing a module:
import math
print(math.sqrt(16))  # 4.0

# Importing specific functions from a module:
from math import pi, sin
print(pi)  # 3.141592653589793
print(sin(pi / 2))  # 1.0

# Aliasing a module:
import math as m
print(m.sqrt(25))  # 5.0

# Creating a module (save as mymodule.py):
"""
# mymodule.py
def greet(name):
    print("Hello, " + name)

person = {
    "name": "Alice",
    "age": 30
}
"""

# Importing a custom module:
import mymodule
mymodule.greet("Bob")
print(mymodule.person["age"])  # 30

# Importing specific parts of a custom module:
from mymodule import greet, person
greet("Charlie")
print(person["name"])  # Alice

# Pip: Python package installer.

# Installing a package:
# Open terminal/command prompt and type:
# pip install requests

# Using an installed package:
import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # 200

# Listing installed packages:
# pip list

# Uninstalling a package:
# pip uninstall requests

# Requirements file: Listing project dependencies.
"""
# requirements.txt
requests==2.25.1
flask==1.1.2
"""

# Installing from a requirements file:
# pip install -r requirements.txt
