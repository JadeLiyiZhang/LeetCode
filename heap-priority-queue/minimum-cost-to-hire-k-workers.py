class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = float('inf')
        WagePerQua = []
        for i in range(len(quality)):
            WagePerQua.append((wage[i] / quality[i], quality[i]))
        
        WagePerQua.sort(key=lambda x: x[0])
        
        maxheap = []
        total_q = 0
        for ratio, q in WagePerQua:
            heapq.heappush(maxheap, -q)
            total_q += q

            if len(maxheap) > k:
                total_q += heapq.heappop(maxheap)

            if len(maxheap) == k:
                res = min(res, round(ratio * total_q, 5))
        
        return res