# given N students with there name and score
# Print the students with second least scores with their names in alphabetical order

students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score]) # Input
    
    
students = sorted(students, key=lambda x: x[1])

#print students
lowest = students[0][1]
#print lowest

for i in range(len(students)):
    if students[i][1] > lowest:
        lowest = students[i][1]
        break
second_students = []        

for student in students:
    if student[1] == lowest:
        second_students.append(student[0])
second_students.sort()        

for student in second_students:
    print student
    
    
