from input  import studentInfo, courseInfo, inputMarks, decompression, zip_compression, load_courses_from_file, load_marks_from_file, load_students_from_file
from output import listCourses, listStudents, showStudentMarks, listStudentsByGPA, decorated_menu

def main():
    if decompression():
        print("Archive found! Loading saved data into memory...")
        students = load_students_from_file()
        courses = load_courses_from_file()
        marks_db = load_marks_from_file()

    else:
        print("No archive found. Starting with empty data.")
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
            zip_compression()
            print("Exiting system.")
            break
        else:
            print("Invalid choice, try again.")
            
        input("\n[Press Enter to return to main menu]")

main()