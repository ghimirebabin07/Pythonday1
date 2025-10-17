# ---------------- LIST ----------------
# ✅ A list is a collection which is ordered and changeable.
# ✅ Allows duplicate elements.

fruits = ["apple", "banana", "cherry"]
print(fruits)                 # Output: ['apple', 'banana', 'cherry']
print(fruits[1])              # Access by index
fruits.append("orange")       # Add item
fruits.remove("banana")       # Remove item
print(fruits)
print(len(fruits))            # Length of list

# Slicing
print(fruits[0:2])            # Get part of list
# Iterating
for item in fruits:
    print(item)

# ---------------- TUPLE ----------------
# ✅ A tuple is ordered and unchangeable.
# ✅ Allows duplicate elements.

numbers = (10, 20, 30, 40)
print(numbers)
print(numbers[0])             # Access element
print(len(numbers))           # Length
print(numbers[1:3])           # Slicing
# Tuples are immutable → numbers[1] = 25 ❌ not allowed

# ---------------- SET ----------------
# ✅ A set is unordered and unindexed.
# ✅ No duplicate elements.

myset = {1, 2, 3, 3, 4}
print(myset)                  # Output: {1, 2, 3, 4}
myset.add(5)                  # Add element
myset.remove(2)               # Remove element
print(myset)

# Set operations
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)                  # Union
print(A & B)                  # Intersection
print(A - B)                  # Difference

# ---------------- DICTIONARY ----------------
# ✅ A dictionary stores data as key-value pairs.
# ✅ Keys are unique, values can repeat.

student = {
    "name": "Babin",
    "age": 20,
    "course": "Python"
}
print(student)
print(student["name"])        # Access by key
student["age"] = 21           # Modify value
student["city"] = "Kathmandu" # Add new pair
print(student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)

# Get all keys and values
print(student.keys())
print(student.values())
