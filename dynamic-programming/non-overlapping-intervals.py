class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        if intervals is None:
            return 0
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                res += 1
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])
        return res