class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        seen = set()
        def dfs(x, y, d, path):
            if x < 0 or x >= row or y < 0 or y >= col:
                return
            if grid[x][y] == 0:
                return
            if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                path.append(d)
                grid[x][y] = 0
                dfs(x + 1, y, "D", path)
                dfs(x - 1, y, "U", path)
                dfs(x, y + 1, "R", path)
                dfs(x, y - 1, "L", path)
                path.append("B")

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, "S", path)
                    seen.add(''.join(path))

        return len(seen)