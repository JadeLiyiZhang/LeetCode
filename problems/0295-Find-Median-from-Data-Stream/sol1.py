# ==========================================================
# 295. Find Median from Data Stream
# Difficulty : Hard
# Language   : Python
# Solution   : #1
# Runtime    : 1307 ms (Beats 8%)
# Memory     : 43.2 MB (Beats 12%)
# Link       : https://leetcode.com/problems/find-median-from-data-stream/
# ==========================================================

class MedianFinder:

    def __init__(self):
        self.stream = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.size += 1

    def findMedian(self) -> float:
        self.stream.sort()
        if self.size % 2 == 1:
            middle_point = (self.size + 1) // 2 - 1
            return self.stream[middle_point]
        else:
            middle_point_1 = self.size // 2 - 1
            middle_point_2 = self.size // 2
            return (self.stream[middle_point_1] + self.stream[middle_point_2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()