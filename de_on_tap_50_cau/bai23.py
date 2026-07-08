def evaluate(tokens):
    stack = []

    for t in tokens:
        if t not in "+-*/":
            stack.append(int(t))
        else:
            b = stack.pop()
            a = stack.pop()

            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(a // b)

    return stack[0]


expr = ["3", "4", "+", "2", "*"]

print(evaluate(expr))