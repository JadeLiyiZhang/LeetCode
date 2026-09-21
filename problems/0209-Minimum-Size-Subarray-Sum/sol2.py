# ==========================================================
# 209. Minimum Size Subarray Sum
# Difficulty : Medium
# Language   : Python
# Solution   : #2
# Runtime    : 19 ms (Beats 45%)
# Memory     : 30.6 MB (Beats 43%)
# Link       : https://leetcode.com/problems/minimum-size-subarray-sum/
# ==========================================================

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        temp = 0
        res = float('inf')
        for right in range(len(nums)):
            temp += nums[right]
            while temp >= target:
                res = min(res, right - left + 1)
                temp -= nums[left]
                left += 1

        return res if res != float('inf') else 0