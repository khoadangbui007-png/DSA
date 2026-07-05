def two_sum(nums, target):
    d = {}

    for i in range(len(nums)):
        x = target - nums[i]

        if x in d:
            return [d[x], i]

        d[nums[i]] = i


a = [2,7,11,15]

print(two_sum(a,9))