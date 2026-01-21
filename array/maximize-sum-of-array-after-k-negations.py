class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        if k == 0:
            return sum(nums)
        
        else:
            nums.sort()
            carry = k % 2
            nums[0] = nums[0] * (-1) ** carry
            return sum(nums)