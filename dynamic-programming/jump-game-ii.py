class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur_end = 0
        cur_far = 0
        n = len(nums)
        for i in range(n - 1):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                ans += 1
                cur_end = cur_far
        return ans