
def searchRange(nums, target):
    left = 0
    n = len(nums)
    right = n - 1
    mid = 0

    if n == 0:
        return [-1, -1]
    elif n == 1:
        if target == nums[0]:
            return [0, 0]
    else:
        if target > nums[-1]:
            return [-1, -1]
        if target == nums[-1]:
            min_i = search_left(nums, n-1, target)
            return [n - 1 - min_i, n - 1]

        if target < nums[0]:
            return [-1, -1]
        if target == nums[0]:
            max_i = search_right(nums, 0, target)
            return [0, max_i]

        while left < right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid

            elif target > nums[mid]:
                left = mid + 1

            else:
                min_i = search_left(nums, mid, target)
                max_i = search_right(nums, mid, target)
                
                return [mid - min_i, mid + max_i]

    return [-1, -1]

def search_left(arr, index, target):
    min_i = 0
    while True:
        if (index - min_i - 1) >= 0:
            if (arr[index - min_i - 1] == target):
                min_i += 1
            else:
                break
        else:
            break
    return min_i

def search_right(arr, index, target):
    max_i = 0
    while True:
        if (index + max_i + 1) < len(arr):
            if (arr[index + max_i + 1] == target):
                max_i += 1
            else:
                break
        else:
            break
    return max_i

if __name__ == "__main__":
    arr = [1, 4]
    res = searchRange(arr, 4)
    print(res)