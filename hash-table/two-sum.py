class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in table:
                return [i, table[rest]]
            else:
                table[nums[i]] = i
