from math import perm


def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(path):
        if len(path) == len(nums):
            res.append(path)
            return

        for n in nums:
            if n in path:
                continue
            dfs(path + [n])

    dfs([])
    return res

def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []
    perm = []
    count = { n:0 for n in nums }

    for n in nums:
        count[n] += 1

    def dfs():
        if len(perm) == len(nums):
            res.append(perm[:])
            return

        for n in count:
            if count[n] == 0:
                continue
            count[n] -= 1
            perm.append(n)

            dfs()
            
            perm.pop()
            count[n] += 1

    dfs()
    return res