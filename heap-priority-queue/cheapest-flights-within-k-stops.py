from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))
       
        # dist[m][n] = min cost from src to m when used n steps
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[src][0] = 0
        # heap = [price, curr_stop, step_used]
        heap = [(0, src, 0)]
        while heap:
            price, stop, step = heapq.heappop(heap) 

            if stop == dst:
                return price
            if price > dist[stop][step]:
                continue
            if step <= k:
                for neighbor, p in graph[stop]:
                    heapq.heappush(heap, (price + p, neighbor, step + 1))
        return -1

