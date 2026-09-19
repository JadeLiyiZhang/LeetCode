class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                temp = sum(nums[i:j])
                if temp % k == 0:
                    res += 1
        return res