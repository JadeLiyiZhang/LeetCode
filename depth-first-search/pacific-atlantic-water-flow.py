class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        #  Define DFS Function to traverse the matrix and mark the cells reachable
        def dfs(r, c, visit, prevHeight):
            #  Base cases for termination and DFS traversal
            if (
                r < 0
                or r == rows
                or c < 0
                or c == cols
                or (r, c) in visit
                or heights[r][c] < prevHeight
            ):
                return 0
            visit.add((r, c))
            #  Recursive cells for DFS traversal in four directions
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        #  DFS from top and bottom borders 
        for c in range(cols):
            dfs (0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows-1][c])

        #  DFS from left and right borders
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        #  Find cells reachable from both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if ((r, c) in pac and (r, c) in atl):
                    res.append((r, c))
        return res