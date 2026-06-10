def prove_loop_invariant(a):
    n = len(a)
    print(f"Mảng ban đầu: {a}")
    print("-" * 50)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

        num_sorted_elements = i + 1
        sorted_part = a[n - num_sorted_elements:] 
        
        print(f"Sau lượt {num_sorted_elements}: {a}")
        print(f"-> Chứng minh: {num_sorted_elements} phần tử lớn nhất đã về cuối là: {sorted_part}")
        print("-" * 50)
        
    print(f"Kết luận: Mảng đã sắp xếp hoàn chỉnh: {a}")
    return a

mang_test = [5, 1, 4, 2, 8]
prove_loop_invariant(mang_test)