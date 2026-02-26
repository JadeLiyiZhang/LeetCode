class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for i, step in enumerate(nums):
            if furthest < i:
                return False
            furthest = max(furthest, i + step)
        return True