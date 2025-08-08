# make a program using oop concpt by create a class name Student and make a constructor and function base also need to ask input from the user with options like add new student,( update student and delete student ) using roll no, show all students and exit, also make a menu for the user and use while loop to call the function again and again until the user wants to exit need to record file in txt format and also need to save the data in the file and load the data from the file
import os
class student:
    def __init__(self,name,age,roll, marks):
        self.name= name
        self.age= age
        self.roll= roll
        self.marks= marks
    def __str__(self):
        return f"name : roll no:{self.roll} , {self.name},age : {self.age}, ,arls : {self.marks}"#direclty printed when obj is printed
    def addstudent():
        
        fs=open("student.txt","a")
        #take input
        name=input("enter name ")
        roll =input("enter name ")
        age= input("enter name ")
        marks =input("enter name ")
        student = student(name , roll , age , marks)
        
    def updatestudent():
        pass
    def deletestudent():
        pass
    def allstudent():
        try:
            with open("student,txt","r")as fs:
                print(fs.read())
        except FileNotFoundError:
            print("no students found")
                
    
    print("MENU : ")
    print("1. ADD STUDENT : ")
    print("2. UPDATE STUDETS DEATILS : ")
    print("3. DELETE STUDENT : ")
    print("4. ALL STUDENT INFO : ")
    print("5. EXIT MENU  ")
    print("SELECT YOUR OPTION : ")
    choice= int(input("enter your choice : "))
     
    match choice :
        case 1:
            addstudent()
        case 2:
            updatestudent()
        case 3:
            deletestudent()
        case 4:
            allstudent()
        case 5: 
            exit()
        case _ :
            print("out of range")
            #__init__->cosntructor
            #__str__->string representation
            #__len__->length
            #__add__->addition
            #__sub__->subtra
            #__mul__->multi
        
  """
  import os

class Student:
    def __init__(self, name, rollno, age, courses, marks):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.courses = courses
        self.marks = marks

    def __str__(self):
        return f"{self.name}, {self.rollno},{self.age},{self.courses},{self.marks}"
    
    def printDetails(self):
        return f"{self.name}, {self.rollno},{self.age},{self.courses},{self.marks}"
    
def addStudent():
    try:
        with open("student.txt", "a") as f:
            name = input("Enter student name: ")
            rollno = input("Enter student rollno: ")
            age = input("Enter student age: ")
            courses = input("Enter student courses: ")
            marks = input("Enter student marks: ")
            student = Student(name, rollno, age, courses, marks)
            f.write(student.printDetails())
            f.write("\n")
            
    except Exception as e:
        print(e)

def serchStudent():
    pass
def deleteStudent():
    pass
def updateStudent():
    pass
def showAllStudents():
    try:
        with open("student.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No students found.")


def menu():
    while True:
        print("----- Welcome to student management system -----")
        print("1. Add New Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Show All Students")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            addStudent()
        elif choice == 2:
            serchStudent()
        elif choice == 3:
            deleteStudent()
        elif choice == 4:
            updateStudent()
        elif choice == 5:
            showAllStudents()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

    print("----- Thank you for using student management system -----")

if __name__ == "__main__":
    menu()
  """      
    
    