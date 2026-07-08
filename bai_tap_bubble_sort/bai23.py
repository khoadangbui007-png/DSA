def analyze_bubble_sort(arr_input):
    a = list(arr_input)
    n = len(a)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
            
    return comparisons, swaps

sorted_case = [1, 2, 3, 4, 5]
random_case = [3, 5, 1, 4, 2]
reverse_case = [5, 4, 3, 2, 1]

print("Kết quả Bài 23 (So sánh hiệu năng):")
print("- Đã sắp xếp (Best): ", analyze_bubble_sort(sorted_case))
print("- Ngẫu nhiên (Average):", analyze_bubble_sort(random_case))
print("- Sắp xếp ngược (Worst):", analyze_bubble_sort(reverse_case))