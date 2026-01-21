class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        maxH = 0
        for i in reversed(range(len(heights))):
            if heights[i] > maxH:
                maxH = heights[i]
                res.append(i)
        return list(reversed(res))