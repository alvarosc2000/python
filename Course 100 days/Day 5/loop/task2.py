student_score =  [123,321,32,431,435,563,12,31,98,32,43,5,6,73,234,642,674]

total_exam_score = sum(student_score)

max_score = 0

for score in student_score:
    if score > max_score:
        max_score = score

print(max_score)
print(max(student_score))