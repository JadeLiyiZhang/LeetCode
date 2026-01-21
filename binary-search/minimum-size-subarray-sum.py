class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = 0
        right = 0
        temp_sum = 0
        for right in range(len(nums)):
            temp_sum += nums[right]
            while temp_sum >= target:
                min_len = min(min_len, right - left + 1)
                temp_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0