from random import randint
import json

#create random scores for the students
NAMES = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# {new_key:new_value for keys in list_of_key}
studentes_scores = {student:randint(1, 100) for student in NAMES}
print(studentes_scores)

studentes_scores_pass = []
for key,value in studentes_scores.items():
    if value > 80:
        studentes_scores_pass.append(key)

students_scores_pass_2 = {student:score for (student, score) in studentes_scores.items() if score > 60}

print(studentes_scores_pass)
print(students_scores_pass_2)

#jump to json the students who pass
with open('personal.json', 'w') as json_file:
    json.dump(students_scores_pass_2, json_file, indent=4)
