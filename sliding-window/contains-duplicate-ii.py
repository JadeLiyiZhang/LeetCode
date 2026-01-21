class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i in range(len(nums)):
            if nums[i] in table:
                if i - table[nums[i]] <= k:
                    return True
                else:
                    table[nums[i]] = i
            else:
                table[nums[i]] = i
        return False