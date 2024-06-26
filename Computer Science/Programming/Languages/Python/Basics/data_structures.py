""" Explaining python data structures """

# Lists: Ordered, changeable, allows duplicates.
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Access by index
fruits[1] = "blueberry"  # Change item
fruits.append("orange")  # Add item
fruits.remove("apple")  # Remove item
print(len(fruits))  # Length
for fruit in fruits:
    print(fruit)  # Iterate

# Tuples: Ordered, unchangeable, allows duplicates.
colors = ("red", "green", "blue")
print(colors[1])  # Access by index
# colors[1] = "yellow"  # Error: Tuples are immutable
print(len(colors))  # Length
for color in colors:
    print(color)  # Iterate

# Dictionaries: Unordered, changeable, no duplicates.
person = {"name": "John", "age": 30}
print(person["name"])  # Access by key
person["age"] = 31  # Change value
person["gender"] = "male"  # Add key-value pair
del person["name"]  # Remove key-value pair
print(len(person))  # Length
for key in person:
    print(key, person[key])  # Iterate

# Sets: Unordered, unchangeable (but can add/remove), no duplicates.
animals = {"cat", "dog", "bird"}
print("cat" in animals)  # Check membership
animals.add("fish")  # Add item
animals.remove("dog")  # Remove item
print(len(animals))  # Length
for animal in animals:
    print(animal)  # Iterate
