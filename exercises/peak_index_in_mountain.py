def peakIndexInMountainArray(self, arr: list[int]) -> int:
    max_ind = 0
    max_val = -1
    for i, val in enumerate(arr):
        if max_val < val:
            max_ind = i
            max_val = val
        else:
            break
            
def peakIndexInMountainArrayBnSrch(arr):
    n = len(arr)
    l = 0
    r = n - 1
    while l < r:
        m = (l + r) // 2
        if m - 1 > 0 and arr[m-1] > arr[m]:
            r = m
        elif m + 1 < n - 1 and arr[m+1] > arr[m]:
            l = m
        else:
            return m
