def sort_students(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j][1] < students[j + 1][1]:
                students[j], students[j + 1] = students[j + 1], students[j]
            elif students[j][1] == students[j + 1][1]:
                if students[j][0] > students[j + 1][0]:
                    students[j], students[j + 1] = students[j + 1], students[j]
    return students

a = [('An', 8), ('Ba', 9), ('Cu', 8)]
print(sort_students(a))  