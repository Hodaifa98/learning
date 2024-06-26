""" Explaining python strings and formatting """

# Looping through a string:
word = "Hello"
for n in word:
    print(n)

# Get length:
len(word)

# Check if a string contains another string:
print("lo" in word)     # => True
print("x" not in word)  # => True

# Slicing strings:
print(word[0:3]) # => "Hel"
print(word[:2])  # => "He" (From start)
print(word[2:])  # => "llo" (To the end)

# Negative indexing:
#  H  e  l  l  o
# -5 -4 -3 -2 -1
print(word[-4:-2]) # => "el" (doesn't include -2)

# Methods to modify strings:
sentence = "Hello World! "
print(sentence.upper())               # => "HELLO WORLD! "
print(sentence.lower())               # => "hello world! "
print(sentence.strip())               # => "Hello World!"
print(sentence.replace("H", "Y"))     # => "Yello World! "
print(sentence.split(" "))            # => ["Hello", "World!", ""]

# Strings formatting using F-Strings:
n = 10
print(f"n is equal to {n}")

# Value modifiers in formatting:
price = 15.75
print(f"Price is: {price:.1f}")  # => "15.8"

# Escaping characters (with backslash \):
print("This is a double quote \"")

# Other escape characters: \\ (Backslash) \n (New line) \t (Tab)

# String Formatting: Formatting strings in Python.

# Using f-strings (formatted string literals):
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Formatting numbers:
pi = 3.14159265359
print(f"The value of pi is approximately {pi:.2f}")  # Two decimal places

# Using format() method:
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

# Specifying positions:
print("My name is {0} and I am {1} years old. {1} is my age.".format(name, age))

# Named placeholders:
print("My name is {name} and I am {age} years old.".format(name="Charlie", age=35))

# Alignment and padding:
print("{:<10}".format("left"))  # Left aligned
print("{:>10}".format("right"))  # Right aligned
print("{:^10}".format("center"))  # Center aligned
print("{:*^10}".format("center"))  # Center aligned with padding

# Formatting with dictionaries:
person = {"name": "Eve", "age": 28}
print("My name is {name} and I am {age} years old.".format(**person))

# Formatting with format specifiers:
number = 12345.6789
print("Formatted number: {:.2f}".format(number))  # Two decimal places
print("Exponential notation: {:.2e}".format(number))  # Exponential notation
print("Hexadecimal: {:x}".format(255))  # Hexadecimal

# Using old-style formatting (%):
name = "Frank"
age = 40
print("My name is %s and I am %d years old." % (name, age))

