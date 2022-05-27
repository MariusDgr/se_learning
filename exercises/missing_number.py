def find_missing(nums):
    present = [False] * (len(nums) + 1)
    for val in nums:
        present[val] = True
    
    # now find missing:
    for i, val in enumerate(present):
        if val is False:
            return i

if __name__ == "__main__":
    arr = [3, 0, 1]
    print(find_missing(arr))