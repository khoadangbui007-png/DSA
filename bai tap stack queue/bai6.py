def Bai_6():
    print("--- Bài 6: Dấu ngoặc cân bằng ---")
    def is_balanced(s):
        brackets_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in brackets_map.values():
                stack.append(char)
            elif char in brackets_map.keys():
                if not stack or stack[-1] != brackets_map[char]:
                    return False
                stack.pop()
        return len(stack) == 0

    print(f"Kiểm tra '([]{{}})': {is_balanced('([]{})')}")
    print(f"Kiểm tra '([)]': {is_balanced('([)]')}")
    print()


if __name__ == '__main__':
    Bai_6()
