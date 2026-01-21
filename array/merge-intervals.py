class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        intervals.sort(key=lambda x:x[0])
        res = []
        cur_end = intervals[0][1]
        cur_start = intervals[0][0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur_end:
                cur_end = max(cur_end, intervals[i][1])
            else:
                res.append([cur_start, cur_end])
                cur_start = intervals[i][0]
                cur_end = intervals[i][1]
        
        res.append([cur_start, cur_end])
        return res