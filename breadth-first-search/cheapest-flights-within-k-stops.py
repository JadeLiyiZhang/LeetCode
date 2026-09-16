from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))
        # heap = [price, curr_stop, step_used]
        heap = [(0, src, 0)]
        while heap:
            price, stop, step = heapq.heappop(heap) 

            if stop == dst:
                return price
            if step <= k:
                for neighbor, p in graph[stop]:
                    heapq.heappush(heap, (price + p, neighbor, step + 1))
        return -1

