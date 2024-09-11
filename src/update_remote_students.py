from copy import deepcopy

def update_remote_students(students):
    students_copy = deepcopy(students)
    for student in students_copy:
        if "location" not in student:
            student["location"] = "remote"
    return students_copy