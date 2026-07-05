def remove_duplicate(nums):
    seen = set()
    ans = []

    for x in nums:
        if x not in seen:
            seen.add(x)
            ans.append(x)

    return ans


a = [3,1,3,2,1]

print(remove_duplicate(a))