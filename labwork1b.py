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
        course_info.append({'id': cid, 'name': name})
    return course_info


def listCourses(courses):
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")


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
        if course['id'] == selected_course:  # Fixed: course['id'] instead of courses['id']
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
        mark = float(input(f"Enter mark for {s_name} (ID: {s_id}): "))
        marks_db[selected_course][s_id] = mark


def showStudentMarks(courses, students, marks_db):
    listCourses(courses)
    selected_course = input("\nSelect a Course ID to view marks: ").strip()

    print(f"\n--- Marks for Course ID: {selected_course} ---")
    for student in students:
        s_id = student['id']
        s_name = student['name']
        mark = get_student_mark(marks_db, selected_course, s_id)
        print(f"Student: {s_name} (ID: {s_id}) | Mark: {mark}")


def main():
    students = studentInfo()
    courses = courseInfo()
    marks_db = {}  

    while True:
        print("\n=== Menu ===")
        print("1. List Students")
        print("2. List Courses")
        print("3. Input Marks for a Course")
        print("4. Show Student Marks for a Course")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            listStudents(students)
        elif choice == '2':
            listCourses(courses)
        elif choice == '3':
            inputMarks(courses, students, marks_db)
        elif choice == '4':
            showStudentMarks(courses, students, marks_db)
        elif choice == '5':
            print("Exiting system.")
            break
        else:
            print("Invalid choice, try again.")

main()