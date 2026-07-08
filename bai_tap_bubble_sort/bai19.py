def min_passes_nearly_sorted(a):
    n = len(a)
    correct_positions = sorted([(val, idx) for idx, val in enumerate(a)])
    
    max_backward_dist = 0
    for current_idx, (val, original_idx) in enumerate(correct_positions):
        dist = original_idx - current_idx
        if dist > max_backward_dist:
            max_backward_dist = dist
            
    return max_backward_dist if max_backward_dist > 0 else 1

a = [1, 2, 3, 5, 4]
print(min_passes_nearly_sorted(a))  