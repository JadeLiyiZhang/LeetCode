from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        kept_nums = deque()
        for i in range(len(nums)):
            self.update_max_nums(kept_nums, nums[i])
            if i >= k and nums[i - k] == kept_nums[0]:
                kept_nums.popleft()
            if i >= k - 1:
                res.append(kept_nums[0])
        return res


    def update_max_nums(self, kept_nums, num):
        while kept_nums and num > kept_nums[-1]:
            kept_nums.pop()
        kept_nums.append(num)