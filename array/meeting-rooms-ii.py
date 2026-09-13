class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        intervals.sort()
        res = 1
        heap = [intervals[0][1]]
        for start, end in intervals[1:]:
            if start < heap[0]:
                res += 1
                heapq.heappush(heap, end)
                print(heap)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
        return res