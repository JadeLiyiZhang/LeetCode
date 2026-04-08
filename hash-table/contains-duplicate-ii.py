class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i in range(len(nums)):
            if nums[i] not in table:
                table[nums[i]] = i
            else:
                gap = i - table[nums[i]]
                if gap <= k:
                    return True
                else:
                    table[nums[i]] = i
        return False