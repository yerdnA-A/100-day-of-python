import random

names = ['Andrey', 'Rhian', 'Lima', 'Caio', 'Lucas']

students_score = {student:random.randint(0,10) for student in names}

print(students_score)

passed_students = {student:score for (student,score) in students_score.items() if score >= 6}
print(passed_students)