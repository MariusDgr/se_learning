def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(i, path):
        res.append(path)
        for j in range(i, len(nums)):
            dfs(j + 1, path + [nums[j]])
    dfs(0, [])
    return res