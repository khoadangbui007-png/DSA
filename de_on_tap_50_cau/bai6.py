def can_split(nums, k, limit):
    count = 1
    total = 0

    for x in nums:
        if total + x > limit:
            count += 1
            total = x
        else:
            total += x

    return count <= k


def split_array(nums, k):
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2

        if can_split(nums, k, mid):
            right = mid
        else:
            left = mid + 1

    return left


nums = [7, 2, 5, 10, 8]
k = 2

print(split_array(nums, k))