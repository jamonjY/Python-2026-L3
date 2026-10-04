from input  import studentInfo, courseInfo, inputMarks
from output import listCourses, listStudents, showStudentMarks, listStudentsByGPA, decorated_menu

def main():
    students = studentInfo()
    courses = courseInfo()
    marks_db = {}  

    while True:
        
        choice = decorated_menu()
        
        if choice == '1':
            listStudents(students)
        elif choice == '2':
            listCourses(courses)
        elif choice == '3':
            inputMarks(courses, students, marks_db)
        elif choice == '4':
            showStudentMarks(courses, students, marks_db)
        elif choice == '5':
            listStudentsByGPA(students, courses, marks_db)
        elif choice == '6':
            print("Exiting system.")
            break
        else:
            print("Invalid choice, try again.")
            
        input("\n[Press Enter to return to main menu]")

main()