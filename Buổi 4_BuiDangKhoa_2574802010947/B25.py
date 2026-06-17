
def verify_loop_invariant(a):
    n = len(a)
    
   
    print("Trạng thái trước vòng lặp (i = -1):")
    print(f" Mảng hiện tại: {a}")
    print(f" Đoạn a[0..-1]: [] (Rỗng -> Thỏa mãn chứa 0 phần tử nhỏ nhất đúng thứ tự)\n")
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        
        
        current_prefix = a[:i + 1]
        remaining_part = a[i + 1:]
        
        
        is_sorted = all(current_prefix[k] <= current_prefix[k + 1] for k in range(len(current_prefix) - 1))
       
        is_smallest = all(x <= y for x in current_prefix for y in remaining_part) if remaining_part else True
        
        print(f"Sau vòng lặp thứ i = {i}:")
        print(f" Mảng hiện tại: {a}")
        print(f" Đoạn a[0..{i}]: {current_prefix}")
        print(f" Kiểm tra tính đúng đắn của bất biến: {is_sorted and is_smallest}")
        print(f" -> Đoạn chứa {i + 1} phần tử nhỏ nhất của mảng theo đúng thứ tự.\n")

data = [5, 3, 1, 4, 2]
verify_loop_invariant(data)