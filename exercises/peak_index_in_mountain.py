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
        
    if n == 0:
        return None
    
    if n == 1:
        return 0
    
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if m - 1 >= 0 and arr[m-1] > arr[m]:
            r = m - 1
        elif m + 1 <= n - 1 and arr[m+1] > arr[m]:
            l = m + 1
        else:
            return m
