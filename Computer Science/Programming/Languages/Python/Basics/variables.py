""" Explaining python variables """

# Variables are created the moment a value is assigned.
n = 10
name = "M"

# Variables can change types.
n = "string"
name = 20

# To specify a data type, we use casting.
x = str(10)     # => "10"
y = int(20)     # =>  20
z = float(30)   # =>  30.0

# Get a data type.
print(x)   # => <class 'str'>
print(y)   # => <class 'int'>
print(z)   # => <class 'float'>

# Strings can use both single and double quotes: '' or "".

# Variable names are case-sensitive: a # A.
# Must start with a letter/underscore and only
# contain alpha-numeric character and underscores.

# Assign multiple values:
a, b, c = "A", "B", "C"
e1 = e2 = e3 = "E"

# Output variables:
print(a)
print(e1, e2, e3)

# Global variables are created outside of a function.
# To create a global variable inside a function, we use "global":
def my_func():
    global m1
    m1 = 100
my_func()
print(m1)

# To change a global variable inside a function, we also use "global":
m2 = 200
def my_func2():
    global m2
    m2 = 300
my_func2()
print(m2)

