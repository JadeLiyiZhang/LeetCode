class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtracking(0, 0, candidates, target, [], res)
        return res

    def backtracking(self, startIndex, cur_sum, candidates, target, path, res):
        if cur_sum == target:
            res.append(path[:])
            return

        if cur_sum > target:
            return

        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            cur_sum += candidates[i]
            self.backtracking(i + 1, cur_sum, candidates, target, path, res)
            path.pop()
            cur_sum -= candidates[i]
