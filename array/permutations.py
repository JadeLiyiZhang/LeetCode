class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, seen):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num not in seen:
                    path.append(num)
                    seen.add(num)
                    dfs(path, seen)
                    path.pop()
                    seen.remove(num)
                
        dfs([], set())
        return res