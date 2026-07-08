def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

if __name__ == "__main__":
    print("Bài 9 - Two Sum:", two_sum([2, 7, 11], 9))  