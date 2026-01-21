from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(start: int, total: int):
            if total == target:
                res.append(path.copy())
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if total + c > target:   # 剪枝
                    break
                path.append(c)
                backtrack(i, total + c)  # 传 i：可重复使用同一元素
                path.pop()

        backtrack(0, 0)
        return res
