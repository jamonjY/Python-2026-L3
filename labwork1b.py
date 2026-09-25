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


def inputMarks(courses, students, marks_db):
    listCourses(courses)
    course_id = input("\nSelect a Course ID to enter marks: ")
    
    # Check if valid course ID
    valid_course = any(c['id'] == course_id for c in courses)
    if not valid_course:
        print("Invalid Course ID!")
        return

    if course_id not in marks_db:
        marks_db[course_id] = {}

    print(f"\nEntering marks for course: {course_id}")
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
        marks_db[course_id][student['id']] = mark


def showStudentMarks(courses, students, marks_db):
    listCourses(courses)
    course_id = input("\nSelect a Course ID to view marks: ")
    
    if course_id not in marks_db or not marks_db[course_id]:
        print("No marks recorded for this course yet!")
        return

    print(f"\n--- Marks for Course ID: {course_id} ---")
    for student in students:
        sid = student['id']
        if sid in marks_db[course_id]:
            print(f"Student: {student['name']} (ID: {sid}) | Mark: {marks_db[course_id][sid]}")


def main():
    students = studentInfo()
    courses = courseInfo()
    marks_db = {}  

    while True:
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