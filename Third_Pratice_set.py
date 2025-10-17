# =====================================================
# 📘 PYTHON PRACTICE SECTION 3
# Topics: Lists | Tuples | Sets | Dictionaries | Functions
# =====================================================

# ---------------- LIST ----------------

# # # # Write the Python program to create and print a list
fruits = ["apple", "banana", "cherry", "orange"]
print("List of fruits:", fruits)

# # # # Write the Python program to access list elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# # # # Write the Python program to modify list element
fruits[1] = "mango"
print("Modified List:", fruits)

# # # # Write the Python program to add and remove elements
fruits.append("grapes")
fruits.remove("apple")
print("Updated List:", fruits)

# # # # Write the Python program to find length and slicing
print("Total fruits:", len(fruits))
print("Sliced list:", fruits[1:3])

# # # # Write a Python program to iterate through a list
for fruit in fruits:
    print("Fruit:", fruit)

# # # # Write a Python program to find max, min, and sum
numbers = [3, 7, 1, 9, 2]
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# ---------------- TUPLE ----------------

# # # # Write the Python program to create and access a tuple
my_tuple = (10, 20, 30, 40)
print("Tuple:", my_tuple)
print("First element:", my_tuple[0])

# # # # Write the Python program to find length and slicing in tuple
print("Length of tuple:", len(my_tuple))
print("Sliced tuple:", my_tuple[1:3])

# # # # Write the Python program to check membership in tuple
if 20 in my_tuple:
    print("20 is present in tuple")

# ---------------- SET ----------------

# # # # Write the Python program to create and print a set
my_set = {10, 20, 30, 40}
print("Set:", my_set)

# # # # Write the Python program to add and remove items from set
my_set.add(50)
my_set.remove(30)
print("Updated Set:", my_set)

# # # # Write the Python program for union, intersection, difference
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)

# # # # Write the Python program to check membership in set
print(3 in A)
print(7 in B)

# ---------------- DICTIONARY ----------------

# # # # Write the Python program to create and print a dictionary
student = {"name": "Babin", "age": 20, "course": "Python"}
print("Student Dictionary:", student)

# # # # Write the Python program to access and modify values
print("Name:", student["name"])
student["age"] = 21
print("Updated Dictionary:", student)

# # # # Write the Python program to add and remove key-value pairs
student["city"] = "Kathmandu"
student.pop("course")
print("After modifications:", student)

# # # # Write the Python program to loop through dictionary keys and values
for key, value in student.items():
    print(key, ":", value)

# # # # Write the Python program to get all keys and values
print("Keys:", student.keys())
print("Values:", student.values())

# ---------------- FUNCTIONS ----------------

# # # # Write the Python program to define and call a simple function
def greet():
    print("Hello! Welcome to Python Functions.")
greet()

# # # # Write the Python program with function having parameters
def add_numbers(a, b):
    print("Sum is:", a + b)
add_numbers(10, 15)

# # # # Write the Python program with function that returns a value
def square(num):
    return num * num
print("Square of 6 is:", square(6))

# # # # Write the Python program with default argument
def welcome(name="User"):
    print("Welcome,", name)
welcome()
welcome("Babin")

# # # # Write the Python program with multiple return values
def calculate(a, b):
    return a + b, a - b, a * b
add, sub, mul = calculate(10, 5)
print("Addition:", add, "Subtraction:", sub, "Multiplication:", mul)

# # # # Write the Python program using function inside loop
def table(num):
    for i in range(1, 6):
        print(num, "x", i, "=", num * i)
table(3)

# # # # Write the Python program to demonstrate local and global variables
x = 100
def show():
    x = 50
    print("Inside function:", x)
show()
print("Outside function:", x)
