class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        prev = nums[0]
        count = 1
        res = 0
        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                count += 1
                prev += 1
            elif nums[i] > prev + 1:
                res = max(res, count)
                prev = nums[i]
                count = 1
            else:
                continue
        return max(res, count)