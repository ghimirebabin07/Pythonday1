# create the new file with w because w helps to create the file and if the file is already
# then it will rewrite or over write the file

f = open("first file.txt","w")
print("File successfuly created")

f.write("Hello My name is Babin Ghimire\n I am Learning python\n Right now i am in the file handling process\n")
f.write("The File handling is Easy and so Powerfull")

#close the file after writing 
f.close 
print('The file is successfully is closed')
f = open("first file.txt","r") #open in r mode for read the file 

# read the content of the file 
content = f.read()
print("File content:")
print(content)
f.close()#close the file after reading 
print("The file is sucessfully closed after reading ") 



# With methods 
print("Using 'with open' methods\n")
with open('first file.txt',"w") as f:
    print("The file is created successfully with 'with open statement'")
    f.write("Hello it's me Babin Ghimire\n  I ma learning file handling in python")
    f.write("The file handling is so powerfull and best\n")
    f.write("The file is close authomatically")
# reading the above file created using with open statement 
with open("first file.txt","r") as f:
    print("The file is successfully open for to read the content ")
    content = f.read()
    print("File content with 'open with':")
    print(content)



