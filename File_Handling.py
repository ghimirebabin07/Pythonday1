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

    #writing csv file 
    import csv 
    with open("First CSV file.txt","w",newline="") as file: 
        writer = csv.writer(file)
        writer.writerow(["Name","Age","Address"]) # Header File 
        writer.writerow(["Babin",19,"Udayapur"])
        writer.writerow(["Sanjana",17,"Udayapur"])
    print("CSV file written Successfully")
    #Reading csv file 
    import csv
    with open ("First CSV file.txt","r") as file:
        reader = csv.reader(file)
        for row in reader: 
            print(row)
    print("CSV file is readed successfully")

import csv

# Write as dictionary
with open("students.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Babin", "Age": 20, "City": "Udayapur"})
    writer.writerow({"Name": "Sanjana", "Age": 18, "City": "Kathmandu"})

# Read as dictionary
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], "is from", row["City"])

import json

data = {
    "name": "Babin",
    "age": 20,
    "skills": ["Python", "C++", "Drawing"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created!")

#reading json 
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)
print("Name:", data["name"])

# Python dict → JSON string
json_data = json.dumps(data, indent=4)
print(json_data)

# JSON string → Python dict
python_data = json.loads(json_data)
print(python_data["skills"])
 
 # Advanced example of error handling in file operations

try:
    # Attempt to open a file
    file = open("example.txt", "r")
    content = file.read()
    print(" File Content:\n", content)

except FileNotFoundError:
    # This block runs if the file is missing
    print(" Error: The file 'example.txt' was not found!")

except PermissionError:
    # This block runs if file exists but you don’t have permission to access it
    print(" Error: You don’t have permission to read this file!")

except Exception as e:
    # Catch any other unexpected error
    print(" An unexpected error occurred:", e)

else:
    # This block runs if no exception occurs
    print(" File read successfully!")

finally:
    # Always executed — whether an error occurred or not
    print("🔚 File operation completed!")
    if 'file' in locals() and not file.closed:
        file.close()
        print(" File closed properly.")
