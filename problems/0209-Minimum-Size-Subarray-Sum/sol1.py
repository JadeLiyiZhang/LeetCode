# ==========================================================
# 209. Minimum Size Subarray Sum
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 18 ms (Beats 51%)
# Memory     : 30.5 MB (Beats 43%)
# Link       : https://leetcode.com/problems/minimum-size-subarray-sum/
# ==========================================================

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        temp = 0
        res = float('inf')
        for right in range(len(nums)):
            temp += nums[right]
            if temp >= target:
                res = min(res, right - left + 1)
                while temp > target and left < right:
                    temp -= nums[left]
                    left += 1
                    if temp >= target:
                        res = min(res, right - left + 1)
        return res if res != float('inf') else 0