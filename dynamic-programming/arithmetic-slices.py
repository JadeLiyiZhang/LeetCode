class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        table = [0] * len(nums)

        for i in range(2, len(nums)):
            diff1 = nums[i] - nums[i-1]
            diff2 = nums[i-1] - nums[i-2]

            if diff1 == diff2:
                table[i] = table[i-1] + 1
                ans += table[i-1] + 1

        return ans