
class Course :
    counter = 1
    def __init__(self, course_name , course_level):
        self._id = Course.counter
        Course.counter +=1
        self.course_name = course_name
        self.course_level = course_level

class Student :
    student_count = 1
    def __init__(self, student_name ,student_level ):
        self.student_id = Student.student_count
        Student.student_count +=1
        self.student_name = student_name
        self.student_level = student_level
        self.student_course = []

    def add_new_course(self, course):
        if course.course_level == self.student_level:
            self.student_course.append(course)
            print("Course successfully added")

        else:
            print("Course level doesn't match the student's level.")

    def display_details(self):
        print(f"Student Name: {self.student_name}\nStudent Level: {self.student_level}\nCourses Enrolled:")
        for course in self.student_course:
            print({course.course_name})
student_list = []
course_list = []


def add_new_student():
        student_name = input("Enter student name: ")
        student_level = input("Select level (A/B/C): ").upper()
        if student_level in ["A", "B", "C"]:
            new_student = Student(student_name, student_level)
            student_list.append(new_student)
            print("Student saved successfully.")
        else:
                print("Invalid level. Please select A, B, or C.")

def remove_student():
        student_id = int(input("Enter student id: "))
        found = False
        for student in student_list:
            if student.student_id == student_id:
                student_list.remove(student)
                print("Delete done successfully.")
                found = True
                break
        if not found:
            print("User does not exist.")
def edit_student():
        student_id = int(input("Enter student id: "))
        found = False
        for student_id in student_list:
            new_name = input("Enter new name: ")
            new_level = input("Select level (A/B/C): ").upper()
            if new_level in ["A", "B", "C"]:
                student_id.student_name = new_name
                student_id.student_level = new_level
                found = True
                print("Student edited successfully.")
            else:
                print("Invalid level. No changes made.")
            break
        if not found:
            print("User does not exist.")

def Display_all_students():
    for student in student_list:
        student.Display_all_students()

def new_Course():
    course_name = input("Enter course name: ")
    while True:
        course_level = input("Select course level (A/B/C): ").upper()
        if course_level in ["A", "B", "C"]:
            break
        else:
            print("Invalid level. Please select A, B, or C.")
    new_course = Course(course_name, course_level)
    course_list.append(new_course)
    print("Course created successfully.")


def Add_Cours():
        student_id = int(input("Enter student id: "))
        found_student = None
        for student in student_list:
            if student.student_id == student_id:
                found_student = student
                break
        if found_student:
            course_id = int(input("Enter course id: "))
            found_course = None
            for course in course_list:
                if course.course_id == course_id:
                    found_course = course
                    break
            if found_course:
                found_student.add_course(found_course)
            else:
                print("Course does not exist.")
        else:
            print("Student does not exist.")



while True:
    print("select choice please")
    print("1-Add new student")
    print("2-Remove student")
    print("3-Edit student")
    print("4-Display all students")
    print("5-Create new course")
    print("6-Add course to student")
    choice = input("Select an option: ")


    if choice == "1":
        add_new_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        edit_student()
    elif choice == "4":
        Display_all_students()
    elif choice == "5":
        new_Course()
    elif choice == "6":
        Add_Cours()