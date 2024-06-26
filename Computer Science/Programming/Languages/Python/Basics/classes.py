""" Explaining python classes """

# Defining a class:
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

# Creating an object:
person1 = Person("Alice", 30)

# Accessing attributes and methods:
print(person1.name)  # Alice
print(person1.age)  # 30
person1.greet()  # Hello, my name is Alice

# Modifying attributes:
person1.age = 31
print(person1.age)  # 31

# Adding methods dynamically:
def say_goodbye(self):
    print("Goodbye from " + self.name)

Person.say_goodbye = say_goodbye
person1.say_goodbye()  # Goodbye from Alice

# Inheritance: Creating a class from another class.
class Student(Person):  # Inherits from Person
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.student_id = student_id

    def study(self):
        print(self.name + " is studying")

# Creating an object of the derived class:
student1 = Student("Bob", 20, "S12345")
print(student1.name)  # Bob
print(student1.student_id)  # S12345
student1.greet()  # Hello, my name is Bob
student1.study()  # Bob is studying

# Method overriding:
class Employee(Person):
    def greet(self):
        print("Hi, I'm " + self.name + " and I work here")

employee1 = Employee("Charlie", 25)
employee1.greet()  # Hi, I'm Charlie and I work here

# Using class and static methods:
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

print(Math.add(5, 3))  # 8
print(Math.multiply(5, 3))  # 15