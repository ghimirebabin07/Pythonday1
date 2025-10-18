def add_student(name):
    with open("students.txt", "a") as f:
        f.write(name + "\n")

def view_students():
    with open("students.txt", "r") as f:
        students = f.readlines()
        print("Student List:")
        for s in students:
            print("-", s.strip())

# Add some students
add_student("Babin")
add_student("Lokendra")
add_student("Rekha")

# View all students
view_students()
