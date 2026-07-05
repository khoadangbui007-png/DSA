def count_frequency(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq

if __name__ == "__main__":
    arr = ['a', 'b', 'a', 'c', 'a']
    print("Bài 3 - Tần suất:", count_frequency(arr))  