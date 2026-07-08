def next_greater(nums):
    stack = []
    ans = [-1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]

        stack.append(nums[i])

    return ans


a = [2, 1, 3]

print(next_greater(a))