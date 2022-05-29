def find_missing(nums):
    present = [False] * (len(nums) + 1)
    for val in nums:
        present[val] = True
    
    # now find missing:
    for i, val in enumerate(present):
        if val is False:
            return i

def findDisappearedNumbers(nums):
    """Space complexity n"""
    found = [False] * len(nums)
    for val in nums:
        found[val-1] = True
    
    res = []
    for i, val in enumerate(found):
        if val == False:
            res.append(i+1)
            
    return res

def findDissappearedNumbers_o1(nums):
    for val in nums:
        i = abs(val) - 1 
        nums[i] = -1 * abs(nums[i])
            
    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i+1)
            
    return res

if __name__ == "__main__":
    arr = [3, 0, 1]
    print(find_missing(arr))