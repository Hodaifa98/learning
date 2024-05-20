""" Explaining python data types """

# Default types:
# Text ===================================> str
# Numeric ================================> int, float, complex
# Sequence ===============================> list, tuple, range
# Mapping ================================> dict
# Set ====================================> set, frozenset
# Boolean ================================> bool
# Binary =================================> bytes, bytearray, memoryview
# None ===================================> NoneType

# Types are set by default at assignement.
# But can also be explicitly set using functions.
# Example: str(10), set(("a", "b", "c"))

# Get a variable type: type(x).

# Create a random number:
import random
print(random.randint(1, 10))

# Multi-line strings:
lines = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit"""

# Strings are arrays:
print(lines[0]) # => "L"
