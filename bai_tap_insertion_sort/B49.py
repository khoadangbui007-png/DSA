
def compare_three_algorithms(origin_arr):
    # Insertion Sort
    def insertion_sort(a):
        arr = a.copy()
        n = len(arr)
        shifts = 0
        comparisons = 0
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0:
                comparisons += 1
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                    shifts += 1
                else:
                    break
            arr[j + 1] = key
        return comparisons, shifts


    def bubble_sort(a):
        arr = a.copy()
        n = len(arr)
        swaps = 0
        comparisons = 0
        for i in range(n):
            for j in range(0, n - i - 1):
                comparisons += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swaps += 1
        return comparisons, swaps

    def selection_sort(a):
        arr = a.copy()
        n = len(arr)
        swaps = 0
        comparisons = 0
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                comparisons += 1
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                swaps += 1
        return comparisons, swaps

    test_data = origin_arr.copy()
    print("Bài 24:")
    print("Insertion Sort (Comparisons, Shifts):", insertion_sort(test_data))
    print("Bubble Sort (Comparisons, Swaps):", bubble_sort(test_data))
    print("Selection Sort (Comparisons, Swaps):", selection_sort(test_data))

compare_three_algorithms([5, 4, 3, 2, 1])