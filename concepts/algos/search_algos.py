def get_closest_value(arr, target):
    """Perform binary search to find the value and index of the
     value in the sorted input array is the closest to the target.
     In case that multiple solutions exist, the rightmost solution is returned."""
    n = len(arr)
    left = 0
    right = n 
    mid = 0

    # edge case - last or above all
    if target >= arr[n - 1]:
        return arr[n - 1], n - 1
    # edge case - first or below all
    if target <= arr[0]:
        return arr[0], 0
    # BSearch solution: Time & Space: Log(N)

    while left < right:
        mid = (left + right) // 2  # find the mid
        if target < arr[mid]:
            right = mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            return arr[mid], mid

    # In case an exact value was not found
    if target < arr[mid]:
        val, elem_index = find_closest(arr[mid - 1], arr[mid], target)
        return val, elem_index + mid - 1
    else:
        val, elem_index = find_closest(arr[mid], arr[mid + 1], target)
        return val, elem_index + mid
 
def find_closest(val1, val2, target):
    """Find the closest value to target between val1 and val2"""
    if target - val1 >= val2 - target:
        return val2, 1  
    else: 
        return val1, 0


if __name__ == "__main__":
    arr = [0, 1, 3, 3, 7, 8]
    res = get_closest_value(arr, 5)
    print(res)

    arr = [0]
    res = get_closest_value(arr, 5)
    print(res)