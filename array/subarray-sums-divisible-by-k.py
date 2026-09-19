class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_table = {0: 1}
        res = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            res += prefix_table.get(prefix_sum % k, 0)
            prefix_table[prefix_sum % k] = prefix_table.get(prefix_sum % k, 0) + 1
        return res