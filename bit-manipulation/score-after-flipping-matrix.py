class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = [0] * n

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        count[0] = m

        for j in range(1, n):
            count_1 = 0
            count_0 = 0
            for i in range(m):
                if grid[i][j] == 1:
                    count_1 += 1
                else:
                    count_0 += 1
            if count_1 < count_0:
                count[j] = count_0
            else:
                count[j] = count_1

        res = 0
        for i in range(len(count)):
            res += count[i] * 2 ** (n - i  - 1)
        
        return res