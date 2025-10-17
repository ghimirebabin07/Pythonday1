# ==============================================
# 🧮 PYTHON PRACTICE SECTION 1
# Topics: Variables | Data Types | Operators
# ==============================================

# # # # Write the Python Program to add the sum of two numbers:
a = 14
b = 67
print("The sum of the two numbers is:", a + b)

# # # # Input version
c = int(input("Enter the first number: "))
d = int(input("Enter the second number: "))
print("The sum of the two numbers is:", c + d)

# # # # Write a Python program to find the remainder when a number is divided by another number
n = 37
z = 5
print('The remainder of the given numbers is:', n % z)

# # # # Check the type of variable assigned using input() function
m = int(input("Enter an integer: "))
e = input("Enter a string: ")
f = float(input("Enter a float number: "))
print("Values are:", m, e, f)
print("Data type of m:", type(m))
print("Data type of e:", type(e))
print("Data type of f:", type(f))

# # # # Write a Python program to demonstrate variable naming rules
student_name = "Babin"
studentAge = 20
_student_country = "Nepal"
print(student_name, studentAge, _student_country)

# # # # Write a Python program to show multiple assignment
x, y, z = 10, 20, 30
print("Values are:", x, y, z)

# # # # Write a Python program to swap two numbers
a = 10
b = 20
a, b = b, a
print("After swapping: a =", a, ", b =", b)

# # # # Write a Python program to calculate simple arithmetic operations
num1 = 25
num2 = 5
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)

# # # # Write a Python program to check all operator types
x, y = 10, 4

# Arithmetic Operators
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Exponent:", x ** y)

# Comparison Operators
print("Is x greater than y?", x > y)
print("Is x equal to y?", x == y)
print("Is x not equal to y?", x != y)

# Logical Operators
a, b = True, False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

# Assignment Operators
num = 10
num += 5
print("After +=:", num)
num -= 3
print("After -=:", num)

# Identity Operators
x = 10
y = 10
print("x is y:", x is y)
print("x is not y:", x is not y)

# Membership Operators
name = "Python"
print("'P' in name:", 'P' in name)
print("'z' not in name:", 'z' not in name)

# # # # Write a Python program to find the average of three numbers entered by the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
avg = (a + b + c) / 3
print("The average is:", avg)

# # # # Write a Python program to check data types of different values
x = 10
y = 5.5
z = "Hello"
w = True
print("Type of x:", type(x))
print("Type of y:", type(y))
print("Type of z:", type(z))
print("Type of w:", type(w))
