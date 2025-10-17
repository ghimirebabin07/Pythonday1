# ----------- LOOPS ------------

# Example 6: Simple for loop
for i in range(5):
    print("Hello", i)

# Example 7: for loop with range(start, stop)
for i in range(1, 6):
    print(i)

# Example 8: while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Example 9: break statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Example 10: continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print("Value:", i)

# Example 11: Nested loop
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")

# Example 12: else with loop
for i in range(3):
    print(i)
else:
    print("Loop finished successfully.")

# Example 13: while with else
num = 1
while num <= 3:
    print("Number:", num)
    num += 1
else:
    print("While loop completed.")