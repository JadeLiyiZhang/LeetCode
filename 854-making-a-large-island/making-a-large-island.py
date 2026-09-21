from collections import defaultdict

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = defaultdict(int)

        def dfs(x, y, island_id):
            if (
                x < 0 or x >= rows or
                y < 0 or y >= cols or
                grid[x][y] != 1
            ):
                return

            grid[x][y] = island_id
            area[island_id] += 1

            dfs(x + 1, y, island_id)
            dfs(x - 1, y, island_id)
            dfs(x, y + 1, island_id)
            dfs(x, y - 1, island_id)

        # 给每个岛屿编号并统计面积
        island_id = 2

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j, island_id)
                    island_id += 1

        # 如果全是 1，已有岛屿面积就是答案
        result = max(area.values(), default=0)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    continue

                # 1 代表当前翻转的这个 0
                current_area = 1
                neighbor_ids = set()

                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if (
                        0 <= x < rows and
                        0 <= y < cols and
                        grid[x][y] > 1
                    ):
                        neighbor_ids.add(grid[x][y])

                for neighbor_id in neighbor_ids:
                    current_area += area[neighbor_id]

                result = max(result, current_area)

        return result