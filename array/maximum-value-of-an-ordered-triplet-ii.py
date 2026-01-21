class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)
        temp_left_max = nums[0]
        res = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > temp_left_max:
                left_max[i] = nums[i - 1]
                temp_left_max = nums[i - 1]
            else:
                left_max[i] = temp_left_max
        temp_right_max = nums[-1]
        for j in range(len(nums) - 2, 0, -1):
            if nums[j + 1] > temp_right_max:
                right_max[j] = nums[j + 1]
                temp_right_max = nums[j + 1]
            else:
                right_max[j] = temp_right_max
        for k in range(1, len(nums) - 1):
            res = max((left_max[k] - nums[k]) * right_max[k], res)
        return res
