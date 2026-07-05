def Bai_13():
    print("--- Bài 13: Trộn các khoảng (Merge Intervals) ---")
    def merge_intervals(intervals):
        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for current in intervals[1:]:
            prev_start, prev_end = merged[-1]
            if current[0] <= prev_end: # Có giao nhau
                merged[-1][1] = max(prev_end, current[1])
            else:
                merged.append(current)
        return merged

    intervals = [[1, 3], [2, 6], [8, 10]]
    print(f"Các khoảng ban đầu: {intervals} -> Sau khi gộp: {merge_intervals(intervals)}")
    print()


if __name__ == "__main__":
    Bai_13()
