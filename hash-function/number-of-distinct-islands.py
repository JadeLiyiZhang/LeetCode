class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        seen = set()
        def dfs(x, y, direction):
            if (x, y) in seen:
                return
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                path.append(direction)
                seen.add((x, y))
                dfs(x + 1, y, "D")
                dfs(x - 1, y, "U")
                dfs(x, y + 1, "R")
                dfs(x, y - 1, "L")
                path.append("0")

        collect = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    path = []
                    dfs(i, j, "0")
                    collect.add(tuple(path))
        return len(collect)


