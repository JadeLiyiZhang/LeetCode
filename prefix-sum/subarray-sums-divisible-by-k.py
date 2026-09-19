class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_table = {0: 1}
        res = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            res += prefix_table.get(remainder, 0)
            prefix_table[remainder] = prefix_table.get(remainder, 0) + 1
        return res