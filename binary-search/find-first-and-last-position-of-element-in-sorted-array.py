class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if nums[right] == target else -1
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left + 1) // 2
                if nums[mid] == target:
                    left = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if nums[left] == target else -1
        
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]