import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:
        graph = defaultdict(list)

        for start, end, price in flights:
            graph[start].append((end, price))

        max_edges = k + 1
        dist = [[float("inf")] * (max_edges + 1) for _ in range(n)]
        dist[src][0] = 0

        heap = [(0, src, 0)]  # price, city, edges_used

        while heap:
            price, city, edges_used = heapq.heappop(heap)

            if city == dst:
                return price

            if price > dist[city][edges_used]:
                continue

            if edges_used == max_edges:
                continue

            for nei, p in graph[city]:
                new_price = price + p
                new_edges = edges_used + 1

                if new_price < dist[nei][new_edges]:
                    dist[nei][new_edges] = new_price
                    heapq.heappush(heap, (new_price, nei, new_edges))

        return -1