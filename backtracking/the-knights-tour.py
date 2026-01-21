class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        board = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(i: int, j: int, k: int) -> bool:
            if k == m * n:
                return True
            for x, y in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
                if 0 <= i + x < m and 0 <= j + y < n and board[i + x][j + y] == -1:
                    board[i + x][j + y] = k
                    if dfs(i + x, j + y, k + 1):
                        return True
                    board[i + x][j + y] = -1
            return False

        board[r][c] = 0
        dfs(r, c, 1)
        return board