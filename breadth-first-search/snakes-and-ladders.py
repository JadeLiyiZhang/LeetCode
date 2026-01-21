from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        cols = list(range(0, n))
        label = 1
        for row in range(n - 1, -1, -1):
            for col in cols:
                cells[label] = (row, col)
                label += 1
            cols.reverse()
        res = [-1] * (n**2 + 1)
        res[1] = 0
        queue = deque([1])
        while queue:
            curr = queue.popleft()
            for nxt in range(curr + 1, min(curr + 6, n * n) + 1):
                row, col = cells[nxt]
                destination = board[row][col] if (board[row][col] != -1) else nxt
                if res[destination] == -1:
                    res[destination] = res[curr] + 1
                    queue.append(destination)
        return res[n * n]
