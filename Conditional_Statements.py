# ----------- CONDITIONAL STATEMENTS ------------

# Example 1: Simple if statement
x = 10
if x > 5:
    print("x is greater than 5")

# Example 2: if-else statement
age = 17
if age >= 18:
    print("You can vote.")
else:
    print("You are not eligible to vote.")

# Example 3: if-elif-else statement
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: Fail")

# Example 4: Nested if statement
num = 8
if num > 0:
    if num % 2 == 0:
        print("Positive Even number")
    else:
        print("Positive Odd number")
else:
    print("Not a positive number")

# Example 5: Short-hand if or Ternary operator
a = 20
b = 15
print("a is greater") if a > b else print("b is greater")