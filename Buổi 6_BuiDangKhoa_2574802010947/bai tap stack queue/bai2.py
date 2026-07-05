def Bai_2():
    print("--- Bài 2: Đảo ngược chuỗi dùng ngăn xếp ---")
    def reverse_string(text):
        stack = list(text)
        reversed_text = ""
        while stack:
            reversed_text += stack.pop()
        return reversed_text

    print(f"Ví dụ: 'abc' -> '{reverse_string('abc')}'") # Kết quả: 'cba'
    print()


if __name__ == '__main__':
    Bai_2()
