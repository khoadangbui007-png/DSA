def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack or stack.pop() != pairs[c]:
                return False

    return len(stack) == 0


print(is_balanced("([]{})"))
print(is_balanced("([)]"))