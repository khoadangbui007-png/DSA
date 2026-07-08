def Bai_8():
    print("--- Bài 8: Tính biểu thức hậu tố (RPN) ---")
    def eval_rpn(expr):
        stack = []
        for token in expr:
            if token.isdigit():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+': stack.append(a + b)
                elif token == '-': stack.append(a - b)
                elif token == '*': stack.append(a * b)
                elif token == '/': stack.append(int(a / b))
        return stack[0]

    print(f"Tính biểu thức '34+': {eval_rpn('34+')}") # Kết quả: 7
    print()


if __name__ == '__main__':
    Bai_8()
