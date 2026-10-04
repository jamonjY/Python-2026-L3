from domains.course import course_exists
from domains.mark import round_mark   



def getNumberStudents():
    return int(input("Enter the number of students: "))


def studentInfo():
    num_students = getNumberStudents()
    students_info = []
    for _ in range(num_students):
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("DoB: ")
        students_info.append({
            'id': sid, 
            'name': name, 
            'dob': dob
        })
    return students_info


def numberCourses():
    return int(input("Enter the number of courses: "))


def courseInfo():
    num_courses = numberCourses()
    course_info = [] 
    for _ in range(num_courses):
        cid = input("Course ID: ")
        name = input("Course Name: ")
        credits_val = int(input("Number of credits: "))
        course_info.append({
            'id': cid, 
            'name': name, 
            'credits': credits_val
        })
    return course_info

def inputMarks(courses, students, marks_db):
    selected_course = input("\nSelect a Course ID to begin with: ")

    if not course_exists(courses, selected_course):
        print("Invalid course id!")
        return 
    
    if selected_course not in marks_db:
        marks_db[selected_course] = {}
    
    for student in students:
        s_id = student['id']
        s_name = student['name']
        raw_mark = float(input(f"Enter mark for {s_name} (ID: {s_id}): "))
        
        rounded_mark = round_mark(raw_mark)
        marks_db[selected_course][s_id] = rounded_mark