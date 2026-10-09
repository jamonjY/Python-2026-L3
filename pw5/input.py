from domains.course import course_exists
from domains.mark import round_mark   
import zipfile
import os


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
    write_students_data_to_file(students_info)
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
    write_courses_data_to_file(course_info)
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
        write_marks_data_to_file(marks_db)   

def write_students_data_to_file(students):
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s['name']},{s['id']},{s['dob']}\n")

def write_courses_data_to_file(courses):
    with open("courses.txt", "w") as f:
        for c in courses:
            f.write(f"{c['name']},{c['id']},{c['credits']}\n")

def write_marks_data_to_file(marks_db):
    with open("marks.txt", "w") as f:
        for courses_id, student_marks in marks_db.items():
            for student_id, marks in student_marks.items():
                f.write(f"{courses_id},{student_id},{marks}\n")


def load_students_from_file():
    students = []
    with open("students.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                student_name, sid, dob = line.split(",")

                students.append({
                    "id" : sid,
                    "name": student_name,
                    "dob": dob
                })

    return students

def load_courses_from_file():
    courses = []
    with open("courses.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:
                course_name, cid, creds = line.split(",")

                courses.append({
                    "id": cid,
                    "name": course_name,
                    "credits": creds
                })
    return courses


def load_marks_from_file():
    marks_db ={}
    with open("marks.txt","r") as f:
        for line in f:
            line = line.strip()
            if line:
                course_id, student_id, mark = line.split(",")

                if course_id not in marks_db:
                    marks_db[course_id] = {}

                marks_db[course_id][student_id] = mark
    return marks_db

def zip_compression():
    files_to_compress = ["students.txt", "courses.txt", "marks.txt"]

    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_compress:
            if os.path.exists(file):
                zipf.write(file)

def decompression():
    if os.path.exists("students.dat"):
        with zipfile.ZipFile("students.dat", "r") as zipf:
            zipf.extractall()
        return True 
    return False



