def Bai_12():
    print("--- Bài 12: Hình chữ nhật lớn nhất trong histogram ---")
    def largest_rectangle_area(heights):
        stack = []
        max_area = 0
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top_idx = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[top_idx] * width)
        while stack:
            top_idx = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[top_idx] * width)
        return max_area

    h = [2, 1, 5, 6, 2, 3]
    print(f"Histogram h = {h} -> Diện tích lớn nhất: {largest_rectangle_area(h)}") # Kết quả: 10
    print()


if __name__ == '__main__':
    Bai_12()
