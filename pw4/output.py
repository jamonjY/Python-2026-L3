import curses
from domains.student import calculate_gpa
from domains.mark import get_student_mark


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


def listCourses(courses):
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']} | Credits: {c['credits']}")


def listStudents(students):
    print("\n--- List of Students ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def showStudentMarks(courses, students, marks_db):
    listCourses(courses)
    selected_course = input("\nSelect a Course ID to view marks: ")

    print(f"\n--- Marks for Course ID: {selected_course} ---")
    for student in students:
        s_id = student['id']
        s_name = student['name']
        mark = get_student_mark(marks_db, selected_course, s_id)
        print(f"Student: {s_name} (ID: {s_id}) | Mark: {mark}")

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