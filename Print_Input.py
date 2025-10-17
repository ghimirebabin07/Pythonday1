# Print and Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old!")

# ----------- USER INPUT -----------
name = input("Enter your name: ")
print("Welcome,", name)

age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

# Multiple inputs
a, b = input("Enter two numbers separated by space: ").split()
print("You entered:", a, "and", b)

# Multiple integer inputs
x, y = map(int, input("Enter two numbers: ").split())
print("Sum =", x + y)

# Type casting and type check
num = int(input("Enter a number: "))
print("Double of your number is", num * 2)
print("Type of num:", type(num))

# ----------- PRACTICAL MINI PROGRAM -----------
name = input("Enter your name: ")
age = int(input("Enter your age: "))
language = input("Enter your favorite programming language: ")
print(f"Hello {name}, you are {age} years old and you love {language}.")