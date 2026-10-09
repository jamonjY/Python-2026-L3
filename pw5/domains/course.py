def course_exists(courses, selected_course):
    for c in courses:
        if c['id'] == selected_course:
            return True 
    return False


    

