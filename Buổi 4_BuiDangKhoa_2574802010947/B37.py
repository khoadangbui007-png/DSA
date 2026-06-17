
def sort_students_by_score(students):
    arr = students.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Khóa so sánh ở đây là điểm số (chỉ số 1 của tuple)
        while j >= 0 and arr[j][1] > key[1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

students_list = [('An', 8), ('Ba', 5)]
print("Bài 12:", sort_students_by_score(students_list))