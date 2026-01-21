class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = cur_min = total_sum = max_sum = min_sum = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            max_sum = max(max_sum, cur_max)

            cur_min = min(nums[i], cur_min + nums[i])
            min_sum = min(min_sum, cur_min)

            total_sum += nums[i]
        
        if min_sum == total_sum:
            return max_sum
        
        else:
            return max(max_sum, total_sum - min_sum)