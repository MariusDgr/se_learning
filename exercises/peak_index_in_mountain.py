def peakIndexInMountainArray(self, arr: list[int]) -> int:
    max_ind = 0
    max_val = -1
    for i, val in enumerate(arr):
        if max_val < val:
            max_ind = i
            max_val = val
        else:
            break
            
    return max_ind