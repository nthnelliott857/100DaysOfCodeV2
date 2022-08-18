import random
import pandas
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
#
#
# student_scores = {student: random.randint(1, 100) for student in names}
# print(names)
# print(student_scores)
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

student_dict = {
    "student": ["Angela", "Nathan", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (key, value) in student_data_frame.items():
    print(value)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Nathan":
        print(row.score)