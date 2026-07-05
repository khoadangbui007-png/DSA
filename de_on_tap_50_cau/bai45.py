def subarray_sum(nums, k):
    count = 0
    prefix = 0
    d = {0:1}

    for x in nums:
        prefix += x

        if prefix-k in d:
            count += d[prefix-k]

        d[prefix] = d.get(prefix,0)+1

    return count


a = [1,1,1]

print(subarray_sum(a,2))