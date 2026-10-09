import math


def round_mark(raw_mark):
  return math.floor(raw_mark * 10) / 10
  
def get_student_mark(marks_db, course_id, student_id):
    if course_id in marks_db:
        if student_id in marks_db[course_id]:
            return marks_db[course_id][student_id]
    return "No mark"
