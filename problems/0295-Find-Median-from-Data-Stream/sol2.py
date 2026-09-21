# ==========================================================
# 295. Find Median from Data Stream
# Difficulty : Hard
# Language   : Python
# Solution   : #2
# Runtime    : 147 ms (Beats 85%)
# Memory     : 42.2 MB (Beats 41%)
# Link       : https://leetcode.com/problems/find-median-from-data-stream/
# ==========================================================

class MedianFinder:

    def __init__(self):
        self.small_half = []
        self.large_half = []

    def addNum(self, num: int) -> None:
        if not self.small_half or num <= -self.small_half[0]:
            heapq.heappush(self.small_half, -num)
        else:
            heapq.heappush(self.large_half, num)
        if len(self.small_half) > len(self.large_half) + 1:
            heapq.heappush(self.large_half, -heapq.heappop(self.small_half))
        elif len(self.large_half) > len(self.small_half):
            heapq.heappush(self.small_half, -heapq.heappop(self.large_half))

    def findMedian(self) -> float:
        if len(self.small_half) > len(self.large_half):
            return -self.small_half[0]
        else:
            return (-self.small_half[0] + self.large_half[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()