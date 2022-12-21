#accept list of student heights
student_heights = input("Please enter student heights separated by comma:\n").split()


for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

# for loop to sum student heights

heights_sum= 0
for heights in student_heights:
    heights_sum = heights_sum + heights
print (heights_sum)

number_of_students = 0
for n in range(0, len(student_heights)):
    number_of_students = number_of_students + n

print(number_of_students)

average_height = heights_sum / number_of_students

print(average_height)