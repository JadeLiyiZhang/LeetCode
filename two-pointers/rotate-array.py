class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        k = k % len(nums)
        helper(0, len(nums) - 1)
        helper(0, k - 1)
        helper(k, len(nums) - 1)