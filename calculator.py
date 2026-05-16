students = {
    "Rishi": [85, 92, 78],
    "Amit": [90, 88, 95],
    "Priya": [70, 65, 80]
}

for student, grades in students.items():
    average = sum(grades) / len(grades)
    print(student, "- Average:", average)
