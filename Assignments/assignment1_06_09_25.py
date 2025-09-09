# File Handling:
# A school wants to maintain student records using a text file.
 
# You are required to write a Python program that performs the following file handling operations step by step:
 
# 1) Write Operation:
# - Create a file named students.txt.
# - Write details of students (Name, Roll Number, Marks) into the file.
 
# 2) Read Operation:
# - Read the content of students.txt and display it on the screen.
 
# 3) Rename Operation:
# - Rename the file from students.txt to student_records.txt.
 
# 4) Directory Operations:
# - Create a directory called SchoolData.
# - Move the renamed file student_records.txt into this directory.
# - List all files present in SchoolData to confirm the file is inside.
 
# 5) Delete Operation:
# - Delete the file student_records.txt from inside the directory.
 
# Finally, delete the SchoolData directory.
 
# Do create a menu taking the user input and then perform the operation


import os
import shutil

def write_students_file():
    with open("students.txt", "w") as f:
        n = int(input("Enter number of students to record: "))
        for i in range(n):
            name = input(f"Enter name of student {i+1}: ")
            roll = input(f"Enter roll number of student {i+1}: ")
            marks = input(f"Enter marks of student {i+1}: ")
            f.write(f"Name: {name}, Roll No: {roll}, Marks: {marks}\n")
    print("Students data written to students.txt.")

def read_students_file():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            print("\nContents of students.txt:")
            print(f.read())
    else:
        print("students.txt not found!")

def rename_file():
    if os.path.exists("students.txt"):
        os.rename("students.txt", "student_records.txt")
        print("File renamed to student_records.txt.")
    else:
        print("students.txt not found!")

def directory_operations():
    dir_name = "SchoolData"
    file_name = "student_records.txt"
    
    if not os.path.exists(file_name):
        print("student_records.txt not found!")
        return
    
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print("Directory SchoolData created.")

    dest_path = os.path.join(dir_name, file_name)
    shutil.move(file_name, dest_path)
    print(f"{file_name} moved to {dir_name} directory.")

    print("\nFiles in SchoolData directory:")
    print(os.listdir(dir_name))

def delete_operations():
    dir_name = "SchoolData"
    file_path = os.path.join(dir_name, "student_records.txt")

    if os.path.exists(file_path):
        os.remove(file_path)
        print("student_records.txt deleted from SchoolData.")
    else:
        print("student_records.txt not found in SchoolData!")

    if os.path.exists(dir_name):
        os.rmdir(dir_name)
        print("SchoolData directory deleted.")
    else:
        print("SchoolData directory not found!")

def menu():
    while True:
        print("\n===== Student Record File Operations Menu =====")
        print("1. Write student data to file")
        print("2. Read student data from file")
        print("3. Rename file")
        print("4. Directory operations (create/move/list)")
        print("5. Delete file and directory")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            write_students_file()
        elif choice == "2":
            read_students_file()
        elif choice == "3":
            rename_file()
        elif choice == "4":
            directory_operations()
        elif choice == "5":
            delete_operations()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()
