def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(i, path):
        res.append(path)
        for j in range(i, len(nums)):
            dfs(j + 1, path + [nums[j]])
    dfs(0, [])
    return res


def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    def dfs(i, path):
        res.append(path)
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            dfs(j + 1, path + [nums[j]])
    dfs(0, [])
    return res