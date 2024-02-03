from collections import namedtuple
Student = namedtuple('student', ['age', 'name', 'rollno'])
students = []

def add_record():
    name = input("what is the student's name? ")
    age = input("what is the student's age? ")
    rollno = input("what is the student's roll number? ")
    student = Student(name=name, age=age, rollno=rollno)
    student.append(students)
    print("record succesfully added!")

def remove_record():
    rollno = input("what is the roll number of the student you want removed? ")
    for student in students:
        if student.rollno == rollno:
            students.remove (student)
            print("record successfully deleted.")
            break
        else:
            print("record not found.")

def veiw_records():
    for student in students:
        print(student)