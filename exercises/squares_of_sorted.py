"""leetcode 977"""
def sortedSquares(self, nums: List[int]) -> List[int]:
        
    r_i = len(nums) - 1
    l_i = 0
    
    squares = []
    
    while l_i <= r_i:
        if abs(nums[l_i]) > abs(nums[r_i]):
            squares.insert(0, nums[l_i]**2)
            l_i += 1
        else:
            squares.insert(0, nums[r_i]**2)
            r_i -= 1

    return squares