student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if (score >= 91 and score <= 100):
        student_scores[student] = 'Outstanding'
    elif (score < 90 and score >= 81):
        student_scores[student] = 'Exceeds Expectations'
    elif (score < 81 and score >= 71):
        student_scores[student] = 'Acceptable'
    else:
        student_scores[student] = 'Fail'

student_grades = student_scores

for key in student_grades:
    print(f'{key} : {student_grades[key]}')