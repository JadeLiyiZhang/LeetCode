class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        nums.sort()

        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(path, used)
                path.pop()
                used[i] = False
            
        dfs([], used)
        return res