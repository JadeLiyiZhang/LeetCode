class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        res = [float('inf')] * len(nums)
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l += 1
            i -= 1
        return res