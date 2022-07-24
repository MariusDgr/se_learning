"Leetcode 442"
def findDuplicates(self, nums: List[int]) -> List[int]:
    res = []
    
    for n in nums:
        index = abs(n) -1
        if nums[index] < 0:
            res.append(abs(n))
        
        nums[index] = -1 * nums[index]

    return res