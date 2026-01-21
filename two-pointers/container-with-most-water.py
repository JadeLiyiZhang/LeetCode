class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers: left, right -> the left most/ right most vertical lines
        # update the pointers: only the vertical lines being longer can cantian more water
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            # water volumn = width * min height of two sides
            water = (right - left) * min(height[left], height[right])
            res = max(res, water)
            # Move the pointer at the shorter line inward:
            # only by replacing the shorter line with a taller one
            # do we have a chance to increase the area.
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res
