class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        cur_id = 2
        areas = {}
        n = len(grid)
        
        def islandId(x, y, cur_id):
            stack = [(x, y)]
            area = 1
            grid[x][y] = cur_id
            while stack:
                cur_x, cur_y = stack.pop()
                for i, j in directions:
                    new_x, new_y = cur_x + i, cur_y + j
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = cur_id
                        area += 1
                        stack.append((new_x, new_y))
            areas[cur_id] = area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islandId(i, j, cur_id)
                    cur_id += 1

        if len(areas) == 1:
            if areas[2] == n * n:
                return n * n
            else:
                return areas[2] + 1
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count = 1
                    seen = set()
                    for m, n in directions:
                        new_i, new_j = i + m, j + n
                        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] != 0 and grid[new_i][new_j] not in seen:
                            count += areas[grid[new_i][new_j]]
                            seen.add(grid[new_i][new_j])
                    res = max(res, count)
        
        return res