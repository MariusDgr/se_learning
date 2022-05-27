
def merge(intervals):
    if len(intervals) == 0:
        return []

    intervals.sort()

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = merged[-1][1]

        if start <= lastEnd:
            merged[-1][1] = max(lastEnd, end)

        else:
            merged.append([start, end])

    return merged

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    # intervals = [[1,4],[5,6]]
    print(merge(intervals))
    # print([[1,6],[8,10],[15,18]])