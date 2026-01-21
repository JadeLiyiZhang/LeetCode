import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        visited = set()
        heap = [(matrix[0][0], 0, 0)]

        for _ in range(k):
            val, row, col = heapq.heappop(heap)
            if (row + 1, col) not in visited and row + 1 < n:
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
                visited.add((row + 1, col))
            if (row, col + 1) not in visited and col + 1 < n:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
                visited.add((row, col + 1))
        return val
