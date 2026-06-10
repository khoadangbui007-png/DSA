def recover_min_passes(start_arr, end_arr):
    n = len(start_arr)
    max_left_shift = 0
    
    for end_idx, value in enumerate(end_arr):
        start_idx = start_arr.index(value)
        shift = start_idx - end_idx
        if shift > max_left_shift:
            max_left_shift = shift
            
    return max_left_shift

start = [4, 3, 2, 1]
end = [3, 2, 1, 4]
print("Kết quả Bài 24 (Số lượt tối thiểu):", recover_min_passes(start, end)) # Kết quả: 1