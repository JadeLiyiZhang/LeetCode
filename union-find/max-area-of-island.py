class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    max_area = max(max_area, area)
        return max_area


    def dfs(self, grid, x, y):
        area = 1
        grid[x][y] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i, j in directions:
            next_x = x + i
            next_y = y + j

            if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == 1:
                area += self.dfs(grid, next_x, next_y)
        return area