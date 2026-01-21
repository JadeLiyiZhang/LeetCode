import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # if only 1 meeting, then just 1 room
        if len(intervals) == 1:
            return 1
        # sort meetings by start time
        intervals.sort(key=lambda x: x[0])

        # minheap to keep track of released meeting room
        heap = [intervals[0][1]]
        res = 1
        # iterate through meetings
        for i in range(1, len(intervals)):
            end = heap[0]

            # if new meeting's start time is before the earliest end time -> meeting room + 1
            if intervals[i][0] < end:
                res += 1
                heapq.heappush(heap, intervals[i][1])
            # if new meeting's start time is after a meeting ends -> reuse this released room
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i][1])
        return res