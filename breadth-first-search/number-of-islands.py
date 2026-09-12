class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def dfs(x, y):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            grid[x][y] = 0
            for i, j in directions:
                new_x, new_y = x + i, y + j
                if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == "1":
                    grid[new_x][new_y] = 0
                    dfs(new_x, new_y)
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res
