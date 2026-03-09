class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(en(nums) - 2):
            if i > 0:
                break
            if nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            if nums[left] + nums[right] == target:
                res.append([nums[i], nums[left], nums[right]])
            if nums[left] + nums[right] < target:
                left += 1
                while nums[left] == nums[left - 1]:
                    left += 1
            else:
                right -= 1
                while nums[right] == nums[right + 1]:
                    right -= 1
        return res            
