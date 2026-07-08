def largest_rectangle(h):
    stack = []
    max_area = 0

    h.append(0)

    for i in range(len(h)):
        while stack and h[stack[-1]] > h[i]:
            height = h[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area


h = [2, 1, 5, 6, 2, 3]

print(largest_rectangle(h))