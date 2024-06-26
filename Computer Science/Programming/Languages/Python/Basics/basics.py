""" Explaining python basics """

# Booleans:
# In Python, booleans can be True or False.
A = 10 > 5 # True
B = 10 == 5 # False

# Evaluate a value:
bool(A)
# Any string is True except empty strings.
# Any number is True except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# Operators:
# Arithmetic (besides regular operators like + and -):
#   %	    Modulus	            x % y	
#   **	    Exponentiation	    x ** y	
#   //	    Floor division	    x // y

# Assignement:
# =
# +=
# ...
# %=
# //=
# **=
# &=
# ...

# Logical:
# and or not
if A > 10 and A < 20:
    print("Between 10 and 20")
if A == 10 or B == 10:
    print("A or B is equal to 10")
if not (A == 10 and A == 20):
    print("A is neither 10 nor 20")

# Identity (comparaison):
print(A is B)
print(A is not B)

# Membership:
print (10 in [10, 20, 30]) # => True
print ('e' not in 'Hello') # => False

# Bitwise:
# & 	AND                     Sets each bit to 1 if both bits are 1
# |	    OR	                    Sets each bit to 1 if one of two bits is 1
# ^	    XOR	                    Sets each bit to 1 if only one of two bits is 1
# ~	    NOT	                    Inverts all the bits
# <<	Zero fill left shift
# >>	Signed right shift

# Operator Precedence:
# If two operators have the same precedence, the expression is evaluated from left to right.
# Parentheses = highest precedence. Expressions inside parentheses must be evaluated first.
# Other rules resemble math, like multiplication preceding addition.
# ...

# Conditions:
# if-elif-else statements:
if A > 10:
    print("Greater than 10")
elif A == 10:
    print("Equal to 10")
else:
    print("Less than 10")

# One-liner if-else:
print("A is greater than B") if A > B else print("A is not greater than B")


# Loops:
# While loop:
i = 1
while i < 6:
    print(i)
    i += 1  # i = i + 1

# For loop:
for x in range(6):  # 0 to 5
    print(x)

# For loop with list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Nested loops:
adj = ["red", "big", "tasty"]
for a in adj:
    for f in fruits:
        print(a, f)

# Loop control statements:
# Break:
for x in range(6):
    if x == 3:
        break
    print(x)  # Stops at 2

# Continue:
for x in range(6):
    if x == 3:
        continue
    print(x)  # Skips 3

# Pass (placeholder):
for x in [0, 1, 2]:
    pass  # Do nothing
