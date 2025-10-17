# Basic printing
print("Hello Python!")  

# Printing multiple items
print("Name:", "Babin", "Age:", 20)

# Using commas adds spaces automatically
print("I", "love", "Python")

# Using + for string concatenation
print("I love " + "coding")

# Using sep parameter
print("Apple", "Banana", "Mango", sep=", ")

# Using end parameter to continue on same line
print("Hello", end=" ")
print("World!")

# ----------- PRINTING VARIABLES -----------
x = 10
y = 5
print("The value of x is", x)
print("Sum =", x + y)
print("Product =", x * y)

# ----------- FORMATTED PRINTING -----------
name = "Babin"
age = 20
print(f"My name is {name} and I am {age} years old.")           # f-string
print("My name is {} and I am {} years old.".format(name, age)) # format()
print("Value1: {0}, Value2: {1}".format(10, 20))                # format with index

# ----------- ESCAPE SEQUENCES -----------
print("Hello\nWorld")         # New line
print("Hello\tWorld")         # Tab
print("I\'m learning Python") # Single quote