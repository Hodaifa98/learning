""" Explaining python strings """

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


