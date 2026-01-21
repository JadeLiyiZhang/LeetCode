class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                index = stack.pop()
                if not stack:
                    break
                width = (i - stack[-1]) - 1
                bounded_height = min(height[stack[-1]], height[i]) - height[index]
                water += width * bounded_height
            stack.append(i)
        return water