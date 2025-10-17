# ---------------- FUNCTIONS ----------------
# ✅ Functions are used to group code that can be reused.
# ✅ Defined using the 'def' keyword.

def greet():
    print("Hello from function!")

greet()                       # Call the function

# Function with parameters
def add(a, b):
    print("Sum:", a + b)

add(5, 10)

# Function with return value
def square(num):
    return num * num

print("Square of 4:", square(4))

# Default argument
def welcome(name="User"):
    print("Welcome", name)

welcome()
welcome("Babin")

# Function with multiple return values
def calculate(x, y):
    return x + y, x - y, x * y

a, s, m = calculate(10, 5)
print("Add:", a, "Sub:", s, "Mul:", m)

# Local vs Global variable
x = 50
def show():
    x = 10  # Local variable
    print("Inside function:", x)

show()
print("Outside function:", x)
