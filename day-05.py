height_of_students = input("Please insert ther height of the students").split()
# convert an array of string to an array of int
for height in range(0, len(height_of_students)):
    height_of_students[height] = int(height_of_students[height])
print(height_of_students)

# total height of students
total_height = 0
for n in height_of_students:
    total_height += n

# number of students
count_students = 0
for n in height_of_students:
    count_students += 1

print (total_height)
print (count_students)

# find the highest height
highest_height = 0
for n in height_of_students:
    if n > height_of_students:
        highest_height = height_of_students
print(highest_height)

