def Bai_11():
    print("--- Bài 11: Phần tử lớn hơn kế tiếp (NGE) ---")
    def next_greater_element(arr):
        res = [-1] * len(arr)
        stack = [] # Lưu index
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                idx = stack.pop()
                res[idx] = arr[i]
            stack.append(i)
        return res

    a = [2, 1, 3]
    print(f"Mảng a = {a} -> Next Greater Element: {next_greater_element(a)}") # Kết quả: [3, 3, -1]
    print()


if __name__ == '__main__':
    Bai_11()
