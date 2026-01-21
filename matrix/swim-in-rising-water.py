class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minheap = [(grid[0][0], 0, 0)]
        visited = [[0 for _ in range(n)] for _ in range(m)]
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while minheap:
            t, i, j = heapq.heappop(minheap)
            if visited[i][j]:
                continue
            if i == m - 1 and j == n - 1:
                return t
            visited[i][j] = 1
            for dx, dy in dir:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if grid[x][y] <= t:
                        heapq.heappush(minheap, (t, x, y))
                    else:
                        heapq.heappush(minheap, (grid[x][y], x, y))
            