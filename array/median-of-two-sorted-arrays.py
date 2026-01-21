class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        left, right = 0, m
        while left <= right:
            i = left + (right - left) // 2
            j = (m + n + 1) // 2 - i
            minX = float('-inf') if i == 0 else nums1[i - 1]
            minY = float('-inf') if j == 0 else nums2[j - 1]
            maxX = float('inf') if i == m else nums1[i]
            maxY = float('inf') if j == n else nums2[j]

            if minX <= maxY and minY <= maxX:
                if (m + n) % 2 == 0:
                    return (max(minX, minY) + min(maxX, maxY)) / 2
                else:
                    return max(minX, minY)

            if minX > maxY:
                right = i - 1
            if minY > maxX:
                left = i + 1
