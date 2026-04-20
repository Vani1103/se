students = []

def add_student(name):
    students.append(name)
    return students

def get_students():
    return students

def delete_student(name):
    if name in students:
        students.remove(name)
    return students