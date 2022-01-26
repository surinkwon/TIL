students = [0, 0, 0, 0, 0]
total = 0

for score in range(5):
    students[score] = int(input())

for student in students:
    if student < 40:
        student = 40
    total += student
print(int(total / len(students)))