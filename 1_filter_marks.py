student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}

def filter_marks(grade):
    return grade>90
    

intelligent_students = dict(filter(lambda item : filter_marks(item[1]),student_grades.items()))

print(intelligent_students)