class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index, path):
            if index == len(nums):
                res.append(path.copy())
                return
            dfs(index + 1, path)
            path.append(nums[index])
            dfs(index + 1, path)
            path.pop()
        
        dfs(0, [])
        return res