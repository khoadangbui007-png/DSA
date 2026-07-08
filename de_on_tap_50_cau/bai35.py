def merge(intervals):
    intervals.sort()

    ans = [intervals[0]]

    for s, e in intervals[1:]:
        if s <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], e)
        else:
            ans.append([s,e])

    return ans


intervals = [[1,3],[2,6],[8,10]]

print(merge(intervals))