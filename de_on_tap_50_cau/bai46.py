def longest(nums):
    s = set(nums)
    ans = 0

    for x in s:
        if x-1 not in s:
            length = 1

            while x+length in s:
                length += 1

            ans = max(ans,length)

    return ans


a = [100,4,200,1,3,2]

print(longest(a))