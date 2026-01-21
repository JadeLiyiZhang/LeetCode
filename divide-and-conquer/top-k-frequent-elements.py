class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        queue = []
        for num, freq in map.items():
            heapq.heappush(queue, (freq, num))
            if len(queue) > k:
                heapq.heappop(queue)
        
        res = []
        for freq, num in queue:
            res.append(num)
        return res