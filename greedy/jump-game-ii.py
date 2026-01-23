class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0
        step = 1
        for i in range(len(nums)):
            if far <= i:
                far = max(far, i + nums[i])
                if far >= len(nums):
                    return step
            else:
                step += 1
        return step