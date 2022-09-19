def combine(self, n: int, k: int) -> List[List[int]]:

    res = []

    def backtrack(i, path):
        if len(path) == k:
            res.append(path)
            return

        for j in range(i, n + 1):
            backtrack(j + 1, path + [j])

    backtrack(1, [])

    return res


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, path, total):
        if total == target:
            res.append(path)
            return

        for j in range(i, len(candidates)):
            if total + candidates[j] > target:
                continue

            dfs(j, path + [candidates[j]], total + candidates[j])

    dfs(0, [], 0)
    return res


def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res, curr = [], []

    def backtrack(curr, pos, remain):

        if remain == 0:
            return res.append(curr[:])

        prev = -1
        for i in range(pos, len(candidates)):
            if prev == candidates[i]:
                continue
            elif remain - candidates[i] < 0:
                break
            curr.append(candidates[i])
            backtrack(curr, i + 1, remain - candidates[i])
            curr.pop()
            prev = candidates[i]

    backtrack(curr, 0, target)
    return res


def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def dfs(curr, i, tot):
        if tot == target:
            res.append(curr.copy())
            return

        if i >= len(candidates) or tot > target:
            return

        curr.append(candidates[i])
        dfs(curr, i + 1, tot + candidates[i])
        curr.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(curr, i + 1, tot)

    dfs([], 0, 0)
    return res
