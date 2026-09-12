class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        cur_end = intervals[0][1]
        cur_start = intervals[0][0]
        for start, end in intervals:
            if start <= cur_end:
                cur_end = end
            else:
                res.append([cur_start, cur_end])
                cur_start = start
                cur_end = end
        res.append([cur_start, cur_end])
        return res
