def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}
    
    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in sum_freq:
            count += sum_freq[prefix_sum - k]
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
    return count

if __name__ == "__main__":
    print("Bài 12 - Số đoạn con bằng k:", subarray_sum([1, 1, 1], 2))  