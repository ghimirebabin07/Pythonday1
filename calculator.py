import operator

# Supported operations
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# Take user input (e.g. "5 + 3")
expression = input("Enter your calculation (e.g. 5 + 3): ")

# Split by space
parts = expression.split()

if len(parts) == 3:
    a, op, b = parts
    try:
        a = float(a)
        b = float(b)
        if op in ops:
            result = ops[op](a, b)
            print(f"Result: {result}")
        else:
            print("Unsupported operator. Use +, -, *, or /.")
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
else:
    print("Please enter in format: number operator number (e.g. 5 + 3)")
