# ==============================================
# 🔁 PYTHON PRACTICE SECTION 2
# Topics: Conditional Statements | Loops
# ==============================================

# # # # Write a Python program to check whether a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# # # # Write a Python program to check if a person is eligible to vote or not
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("Sorry, you are not eligible to vote yet.")

# # # # Write a Python program to find the largest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# # # # Write a Python program to check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# # # # Write a Python program to check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# # # # Write a Python program to grade marks using if-elif
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# # # # Write a Python program to check whether a character is a vowel or consonant
ch = input("Enter a single character: ").lower()
if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

# # # # Write a Python program using nested if to check if a number is positive and even
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive and Even number")
    else:
        print("Positive but Odd number")
else:
    print("Not a positive number")

# # # # Write a Python program to display numbers from 1 to 10 using for loop
for i in range(1, 11):
    print(i)

# # # # Write a Python program to print even numbers between 1 to 20 using for loop
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# # # # Write a Python program to print odd numbers between 1 to 20 using while loop
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

# # # # Write a Python program to find the sum of first 10 natural numbers using for loop
total = 0
for i in range(1, 11):
    total += i
print("Sum of first 10 natural numbers is:", total)

# # # # Write a Python program to print the multiplication table of a given number
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# # # # Write a Python program to calculate the factorial of a number using while loop
num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial of", num, "is:", fact)

# # # # Write a Python program to find the sum of digits of a number
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10
print("Sum of digits is:", sum_digits)

# # # # Write a Python program to reverse a number using while loop
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed number is:", rev)

# # # # Write a Python program to print stars pattern
for i in range(1, 6):
    print("*" * i)

# # # # Write a Python program to print numbers from 10 to 1 using while loop
i = 10
while i >= 1:
    print(i)
    i -= 1

# # # # Write a Python program using break and continue statements
for i in range(1, 10):
    if i == 5:
        continue   # skip 5
    if i == 8:
        break      # stop loop at 8
    print(i)
