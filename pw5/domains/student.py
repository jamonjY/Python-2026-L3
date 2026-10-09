import math
import numpy as np

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
    
    np_marks = np.array(mark_list, dtype = float)
    np_credits = np.array(credit_list, dtype = float)

    if np_credits.sum() == 0:
        return 0.0

    raw_gpa = np.average(np_marks, weights = np_credits)
    rounded_gpa = math.floor(raw_gpa * 10) / 10

    return rounded_gpa