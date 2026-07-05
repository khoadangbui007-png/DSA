def Bai_14():
    print("--- Bài 14: Bài toán nhịp giá cổ phiếu (Stock Span) ---")
    def stock_span(prices):
        span = []
        stack = [] # Lưu trữ tuple (index, price)
        for i, price in enumerate(prices):
            while stack and stack[-1][1] <= price:
                stack.pop()
            if not stack:
                span.append(i + 1)
            else:
                span.append(i - stack[-1][0])
            stack.append((i, price))
        return span

    gia = [100, 80, 60, 70, 60, 75, 85]
    print(f"Giá cổ phiếu: {gia} \n-> Nhịp giá (Stock Span): {stock_span(gia)}")
    print()


if __name__ == '__main__':
    Bai_14()
