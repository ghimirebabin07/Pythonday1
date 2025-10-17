
# Operators are special symbols used to perform operations on values or variables.

# ---------------- ARITHMETIC OPERATORS ----------------
# Used to perform basic mathematical operations.

a = 15
b = 4

print("Addition:", a + b)         # 19
print("Subtraction:", a - b)      # 11
print("Multiplication:", a * b)   # 60
print("Division:", a / b)         # 3.75
print("Floor Division:", a // b)  # 3 (integer result)
print("Modulus:", a % b)          # 3 (remainder)
print("Exponent:", a ** b)        # 15⁴ = 50625

# ---------------- ASSIGNMENT OPERATORS ----------------
# Used to assign values to variables.

x = 10
x += 5   # same as x = x + 5
print("x after += :", x)

x -= 3   # same as x = x - 3
print("x after -= :", x)

x *= 2
print("x after *= :", x)

x /= 4
print("x after /= :", x)

x %= 3
print("x after %= :", x)

x **= 2
print("x after **= :", x)

# ---------------- COMPARISON OPERATORS ----------------
# Used to compare two values (returns True or False).

a = 10
b = 20

print("a == b:", a == b)   # False
print("a != b:", a != b)   # True
print("a > b:", a > b)     # False
print("a < b:", a < b)     # True
print("a >= b:", a >= b)   # False
print("a <= b:", a <= b)   # True

# ---------------- LOGICAL OPERATORS ----------------
# Used to combine conditional statements.

x = True
y = False

print("x and y:", x and y)   # False
print("x or y:", x or y)     # True
print("not x:", not x)       # False

# ---------------- IDENTITY OPERATORS ----------------
# Used to compare memory locations (object identity).

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is c:", a is c)           # True (same object)
print("a is b:", a is b)           # False (different objects)
print("a is not b:", a is not b)   # True

# ---------------- MEMBERSHIP OPERATORS ----------------
# Used to test if a value is present in a sequence.

nums = [10, 20, 30, 40]

print("20 in nums:", 20 in nums)        # True
print("50 not in nums:", 50 not in nums) # True

# ---------------- BITWISE OPERATORS ----------------
# Used to perform bit-level operations.

a = 5   # Binary: 0101
b = 3   # Binary: 0011

print("a & b:", a & b)   # AND → 0001 → 1
print("a | b:", a | b)   # OR → 0111 → 7
print("a ^ b:", a ^ b)   # XOR → 0110 → 6
print("~a:", ~a)         # NOT → -(a+1) = -6
print("a << 1:", a << 1) # Left shift → 1010 → 10
print("a >> 1:", a >> 1) # Right shift → 0010 → 2
