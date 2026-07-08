def remove_even(nums):
    result = []

    for x in nums:
        if x % 2 != 0:
            result.append(x)

    return result


a = [1,2,3,4,5,6]

print(remove_even(a))