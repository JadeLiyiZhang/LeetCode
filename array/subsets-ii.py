class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(path, index):
            if index == len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[index])
            dfs(path, index + 1)
            path.pop()

            while index < len(nums) - 1 and nums[index + 1] == nums[index]:
                index += 1

            dfs(path, index + 1)
        
        dfs([], 0)
        return res