class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        curDiff = 0
        preDiff = 0
        res = 1
        for i in range(len(nums) - 1):
            curDiff = nums[i + 1] - nums[i]
            if (curDiff < 0 and preDiff >= 0) or (curDiff > 0 and preDiff <= 0):
                res += 1
                preDiff = curDiff
        return res