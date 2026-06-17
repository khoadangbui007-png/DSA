
students = [('An', 8), ('Ba', 5)]
n = len(students)

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
    
        if students[j][1] < students[min_idx][1]:
            min_idx = j
            
  
    students[i], students[min_idx] = students[min_idx], students[i]

print("Danh sách học sinh sau khi sắp xếp:", students)