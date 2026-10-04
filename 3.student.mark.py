import math
import numpy as np 
import curses


def getNumberStudents():
    return int(input("Enter the number of students: "))


def studentInfo():
    num_students = getNumberStudents()
    students_info = []
    for _ in range(num_students):
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("DoB: ")
        students_info.append({'id': sid, 'name': name, 'dob': dob})
    return students_info


def numberCourses():
    return int(input("Enter the number of courses: "))


def courseInfo():
    num_courses = numberCourses()
    course_info = [] 
    for _ in range(num_courses):
        cid = input("Course ID: ")
        name = input("Course Name: ")
        Credits = int(input("Number of credits: "))
        course_info.append({'id': cid, 'name': name, 'credits': Credits})
    return course_info


def listCourses(courses):
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']} | Credits: {c['credits']}")


def listStudents(students):
    print("\n--- List of Students ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")


def get_student_mark(marks_db, course_id, student_id):
    if course_id in marks_db:
        if student_id in marks_db[course_id]:
            return marks_db[course_id][student_id]
    return "No mark"


def inputMarks(courses, students, marks_db):
    listCourses(courses)
    selected_course = input("\nSelect a Course ID to begin with: ")

    course_exists = False
    for course in courses:
        if course['id'] == selected_course:
            course_exists = True
            break

    if course_exists == False:
        print("Invalid course id!")
        return 
    
    if selected_course not in marks_db:
        marks_db[selected_course] = {}
    
    for student in students:
        s_id = student['id']
        s_name = student['name']
        raw_mark = float(input(f"Enter mark for {s_name} (ID: {s_id}): "))
        rounded_mark = math.floor(raw_mark * 10) / 10
        marks_db[selected_course][s_id] = rounded_mark


def showStudentMarks(courses, students, marks_db):
    listCourses(courses)
    selected_course = input("\nSelect a Course ID to view marks: ")

    print(f"\n--- Marks for Course ID: {selected_course} ---")
    for student in students:
        s_id = student['id']
        s_name = student['name']
        mark = get_student_mark(marks_db, selected_course, s_id)
        print(f"Student: {s_name} (ID: {s_id}) | Mark: {mark}")


def gather_student_data(students, marks_db, courses, student_id):
    mark_list = []
    credit_list = []

    student_exists = False
    for s in students:
        if s['id'] == student_id:
            student_exists = True
            break
    
    if not student_exists:
        print("Invalid student ID! ")
        return None, None

    for course_id, student_marks in marks_db.items():
        if student_id in student_marks:
            mark = marks_db[course_id][student_id]

            for c in courses:
                if c['id'] == course_id:
                    mark_list.append(mark)
                    credit_list.append(c['credits'])  
                    break
     
    if not mark_list:
        return None, None

    return mark_list, credit_list


def calculate_gpa(students, courses, marks_db, student_id):
    gpa = 0.0
    mark_list, credit_list = gather_student_data(students, marks_db, courses, student_id)

    if mark_list is None or credit_list is None or len(mark_list) == 0 or len(credit_list) == 0:
        return gpa
    
    np_marks = np.array(mark_list)
    np_credits = np.array(credit_list)

    raw_gpa = np.average(np_marks, weights = np_credits)
#floor function usage here we multiply by 10 to take the integer part and then divide by 10 to separate the fractional part again 
    rounded_gpa = math.floor(raw_gpa * 10) / 10 

    return rounded_gpa


def listStudentsByGPA(students, courses, marks_db):
    if not students:
        print("No students in the system!")
        return

    if not courses or not marks_db:
        print("Error: Not enough information to make rank table.")
        return

    ranked_students = []

    for s in students:
        s_name = s['name']
        s_id = s['id']

        gpa = calculate_gpa(students, courses, marks_db, s_id)
        temporary_dict = {'id': s_id, 'name': s_name, 'gpa': gpa}
        ranked_students.append(temporary_dict)

    ranked_students.sort(key=lambda item: item['gpa'], reverse=True)

    print("\n--- Sorted Students by GPA ---")
    for s in ranked_students:
        print(f"ID: {s['id']} | Name: {s['name']} | GPA: {s['gpa']:.1f}")


def draw_header(stdscr, title):
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, f"=== {title.upper()} ===", curses.A_BOLD)


def decorated_menu():
    def _render(stdscr):
        stdscr.keypad(True)
        curses.cbreak()
        curses.curs_set(0)

        options = [
            "1. List Students",
            "2. List Courses",
            "3. Input Marks for a Course",
            "4. Show Student Marks for a Course",
            "5. List Students by GPA",
            "6. Exit"
        ]
        selected_row = 0

        while True:
            draw_header(stdscr, "Student Management System")
            stdscr.addstr(2, 2, "Use Arrow Keys (UP/DOWN) & Press Enter to select:", curses.A_DIM)

            for idx, option in enumerate(options):
                y_pos = 4 + idx
                if idx == selected_row:
                    stdscr.addstr(y_pos, 4, f"> {option}", curses.A_REVERSE)
                else:
                    stdscr.addstr(y_pos, 4, f"  {option}")

            stdscr.refresh()
            key = stdscr.getch()

            if key == curses.KEY_UP and selected_row > 0:
                selected_row -= 1
            elif key == curses.KEY_DOWN and selected_row < len(options) - 1:
                selected_row += 1
            elif key in (curses.KEY_ENTER, 10, 13, ord('\n'), ord('\r'), ord(' ')):
                return str(selected_row + 1)

    return curses.wrapper(_render)



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