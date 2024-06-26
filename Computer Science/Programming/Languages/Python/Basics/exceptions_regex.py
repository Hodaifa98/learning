""" Explaining python Exceptions & Regex """

# Basic try-except:
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")  # Handles division by zero

# Multiple exceptions:
try:
    a = int("hello")
except (ValueError, TypeError):
    print("An error occurred")  # Handles both ValueError and TypeError

# Catching all exceptions:
try:
    y = 10 / 0
except Exception as e:
    print("An error occurred:", e)  # Prints the error message

# Finally block: Executes regardless of an exception.
try:
    print("Try block")
finally:
    print("Finally block")  # Always executes

# Else block: Executes if no exception occurs.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful:", result)  # Executes because no exception

# Raising exceptions:
try:
    raise ValueError("A custom error message")
except ValueError as e:
    print("Caught an error:", e)

# Custom exceptions:
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print("Caught a custom error:", e)

# Using finally with file operations:
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed")


# Regex: Regular expressions, a powerful tool for matching patterns in text.

import re

# Basic pattern matching:
text = "The rain in Spain"
pattern = "rain"
match = re.search(pattern, text)
print(match)  # <re.Match object; span=(4, 8), match='rain'>

# Finding all matches:
pattern = "ai"
matches = re.findall(pattern, text)
print(matches)  # ['ai', 'ai']

# Splitting a string:
pattern = "\s"  # Split by whitespace
result = re.split(pattern, text)
print(result)  # ['The', 'rain', 'in', 'Spain']

# Replacing substrings:
pattern = "Spain"
replacement = "France"
result = re.sub(pattern, replacement, text)
print(result)  # The rain in France

# Using special characters:
text = "hello world"
pattern = "^hello"  # Matches 'hello' at the start of the string
match = re.search(pattern, text)
print(match)  # <re.Match object; span=(0, 5), match='hello'>

pattern = "world$"  # Matches 'world' at the end of the string
match = re.search(pattern, text)
print(match)  # <re.Match object; span=(6, 11), match='world'>

# Character sets:
text = "The quick brown fox"
pattern = "[aeiou]"  # Matches any vowel
matches = re.findall(pattern, text)
print(matches)  # ['e', 'u', 'i', 'o', 'o']

# Quantifiers:
text = "The quick brown fox"
pattern = "o{2}"  # Matches exactly two 'o's in a row
matches = re.findall(pattern, text)
print(matches)  # []

pattern = "o{1,2}"  # Matches one or two 'o's in a row
matches = re.findall(pattern, text)
print(matches)  # ['o', 'o']

# Groups:
text = "The rain in Spain"
pattern = "(rain|Spain)"  # Matches either 'rain' or 'Spain'
matches = re.findall(pattern, text)
print(matches)  # ['rain', 'Spain']

# Using groups to capture:
pattern = "(\d{4})-(\d{2})-(\d{2})"
text = "2024-06-26"
match = re.search(pattern, text)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")  # Year: 2024, Month: 06, Day: 26

# Compiling regex patterns for efficiency:
pattern = re.compile(r"\d+")
matches = pattern.findall("There are 123 apples and 456 oranges")
print(matches)  # ['123', '456']
