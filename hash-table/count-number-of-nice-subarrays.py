class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        prefix = {0:1}
        odd_count = 0
        ans = 0
        for num in nums:
            if num % 2 ==1:
                odd_count += 1
                ans += prefix.get(odd_count - k, 0)
                prefix[odd_count] = prefix.get(odd_count, 0) + 1
        return ans