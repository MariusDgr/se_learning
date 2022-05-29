def singleNumber3(nums):
    """Crackhead solution"""
    one, two = 0, 0
    for x in nums:
        two = two ^ (one & x)
        one = one ^ x
        mask = ~(two & one)
        
        one, two = mask & one, mask & two
        
    return one

def singleNumber(self, nums: List[int]) -> int:
    res = 0
    for val in nums:
        res = val ^ res
    return res