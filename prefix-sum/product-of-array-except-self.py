class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        
        right = 1
        for j in range(n - 1, -1, -1):
            res[j] = res[j] * right
            right = right * nums[j]
        return res
