class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findFirst(target):
            left, right = 0, len(nums) - 1
            res = float("inf")
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    res = min(res, mid)
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return res

        def findLast(target):
            left, right = 0, len(nums) - 1
            res = float('-inf')
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    res = max(res, mid)
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return res
        
        first = findFirst(target)
        last = findLast(target)
        if first == float('inf'):
            first = -1
        if last == float('-inf'):
            last = -1
        return [first, last]