def containsDuplicate(nums: list[int]) -> bool:
    found = set()
    for val in nums:
        if val in found:
            return True
        found.add(val)
    return False

if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 4, 5]))
    print(containsDuplicate([1, 4, 4, 5]))
