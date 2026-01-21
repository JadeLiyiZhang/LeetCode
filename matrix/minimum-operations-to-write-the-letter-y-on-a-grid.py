class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = set()
        y_table = {0: 0, 1: 0, 2: 0}
        else_table = {0: 0, 1: 0, 2: 0}
        x, y = n // 2, n // 2
        while x >= 0 and y >= 0:
            y_table[grid[x][y]] += 1
            seen.add((x, y))
            x -= 1
            y -= 1

        u, v = n // 2 - 1, n // 2 + 1
        while u >= 0 and n > v >= 0:
            y_table[grid[u][v]] += 1
            seen.add((u, v))
            u -= 1
            v += 1

        m, k = n // 2 + 1, n // 2
        while m < n:
            y_table[grid[m][k]] += 1
            seen.add((m, k))
            m += 1

        for i in range(n):
            for j in range(n):
                if (i, j) not in seen:
                    else_table[grid[i][j]] += 1


        res = float('inf')
        for m in [0, 1, 2]:
            for k in [0, 1, 2]:
                if m == k:
                    continue
                time = 0
                for key in y_table.keys():
                    if key != m:
                        time += y_table[key]
                for key in else_table.keys():
                    if key != k:
                        time += else_table[key]
                res = min(res, time)
        return res