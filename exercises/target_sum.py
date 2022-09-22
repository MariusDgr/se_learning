def findTargetSumWays(self, nums: List[int], target: int) -> int:
    dp = {}

    def backtrack(i, s):
        if i == len(nums):
            if s == target:
                return 1
            else:
                return 0

        if (i, s) in dp:
            return dp[(i, s)]

        dp[(i, s)] = (backtrack(i + 1, s + nums[i]) + 
                      backtrack(i + 1, s - nums[i]))

        return dp[(i, s)]

    return backtrack(0, 0)