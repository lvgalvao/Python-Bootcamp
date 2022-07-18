student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {
}

#TODO-2: Write your code below to add the grades to student_grades.👇

# Score 91-100 grade = "Outstanding"
# Score 81-90 grade = "Exceeds Expectations"
# Score 71-80 grade = "Acceptable"
# Score 0-70 grade = "Normal"

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    elif score>= 0:
        student_grades[student] = "Normal"

# 🚨 Don't change the code below 👇
print(student_grades)
