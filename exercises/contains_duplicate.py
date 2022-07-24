def containsDuplicate(nums: list[int]) -> bool:
    found = set()
    for val in nums:
        if val in found:
            return True
        found.add(val)
    return False

def findDuplicate(self, nums: List[int]) -> int:
    """Floyd's algorithm"""
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break
            
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 4, 5]))
    print(containsDuplicate([1, 4, 4, 5]))
