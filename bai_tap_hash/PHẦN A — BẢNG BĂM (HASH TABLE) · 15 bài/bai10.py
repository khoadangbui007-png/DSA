def first_uniq_char(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
    return -1

if __name__ == "__main__":
    print("Bài 10 - Chỉ số không lặp đầu tiên:", first_uniq_char("leetcode")) 