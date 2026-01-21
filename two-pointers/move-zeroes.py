class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        index = 0
        while cur < len(nums):
            if nums[cur] != 0:
                nums[index] = nums[cur]
                cur += 1
                index += 1
            else:
                cur += 1
        while index < len(nums):
            nums[index] = 0
            index += 1