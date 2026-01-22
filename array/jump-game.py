class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i, strep in enumerate(nums):
            if i > far:
                return False
            far = max(far, i + nums[i])
            if far >= len(nums) - 1:
                return True
        return True