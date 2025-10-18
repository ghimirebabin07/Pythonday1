f = open("my file.txt","w")
f.write("Hello, Babin! This is the new file\n")
f.write("Second time open the file with babin")
f.close()
print('The file Created successfully and Data is Updated:') 


# with statement 
with open("my file.txt","w") as f:
    f.write("Hello babin\n")
    f.write("The file is automatically close after writing ")

print("Done - File closed Automatically")

# Append  
with open("example.txt","w") as g: 
    print("The file is created successfully:")
    g.write("\nHello!\n")
    g.write("\nFirst append\n")
with open("example.txt","a") as g:
    g.write("\nThis line was added after By Me myself")
# Read line by line 
with open("example.txt","r") as g:
    print("Reading line by line ")
    for line in g:
        print(line.strip())     #remove the \n of the last sentence 

# Read all lines into a list 
with open("example.txt", "r") as g:
    lines = g.readlines()

print("📋 File as List of Lines:")
print(lines)

# File Cursor: seek() and tell()
# 🧠 tell() → gives current position
# 🧠 seek(pos) → moves the cursor to a given position (e.g., start, middle)
with open("example.txt", "r") as g :
    print("Current position:", g.tell())   # Start position (0)
    g.read(5)                              # Read 5 characters
    print("After reading 5 chars:", g.tell())
    g.seek(0)                              # Move cursor back to start
    print("After seek(0):", g.tell())