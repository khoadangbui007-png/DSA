def rotate(nums, k):
    k %= len(nums)

    nums[:] = nums[-k:] + nums[:-k]

    return nums


a = [1,2,3,4,5]

print(rotate(a,2))