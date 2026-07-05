def Bai_5():
    print("--- Bài 5: Duyệt và đếm phần tử ---")
    stack = [1, 2, 3]
    temp_stack = []
    count = 0
    
    print("In các phần tử theo thứ tự LIFO: ", end="")
    while stack:
        element = stack.pop()
        print(element, end=" ")
        temp_stack.append(element)
        count += 1
        
    # Khôi phục lại ngăn xếp ban đầu bằng ngăn xếp phụ
    while temp_stack:
        stack.append(temp_stack.pop())
        
    print(f"\nSố phần tử đếm được: {count}")
    print(f"Ngăn xếp gốc được giữ nguyên: {stack}")
    print()


if __name__ == '__main__':
    Bai_5()
