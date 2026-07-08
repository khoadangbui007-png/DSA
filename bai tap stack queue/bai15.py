def Bai_15():
    print("--- Bài 15: Sắp xếp một ngăn xếp ---")
    def sort_stack(stack):
        temp_stack = []
        while stack:
            tmp = stack.pop()
            while temp_stack and temp_stack[-1] > tmp:
                stack.append(temp_stack.pop())
            temp_stack.append(tmp)
        return temp_stack

    stk = [3, 1, 2]
    print(f"Ngăn xếp gốc: {stk} -> Sau khi sắp xếp (đỉnh nhỏ nhất): {sort_stack(stk)}")
    print()


# ==============================================================================
# PHẦN B – HÀNG ĐỢI (QUEUE) - 15 BÀI
# ==============================================================================


if __name__ == '__main__':
    Bai_15()
