students = {
    "Shreyash": 85,
    "Krish": 92,
    "Om": 78,
    "Tanmay": 88,
    "Deepak": 95
}

print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)
print("Class Average:", average)

top_student = max(students, key=students.get)
print("Highest Marks Student:", top_student)
print("Marks:", students[top_student])
