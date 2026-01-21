# Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight

from typing import List


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def same_value(x: int, y: int, length: int) -> bool:
            v = grid[x][y]
            for i in range(x, x + length):
                for j in range(y, y + length):
                    if grid[i][j] != v:
                        return False
            return True

        def solve(x: int, y: int, length: int) -> 'Node':
            if same_value(x, y, length):
                return Node(grid[x][y], True)
            half = length // 2
            tl = solve(x, y, half)
            tr = solve(x, y + half, half)
            bl = solve(x + half, y, half)
            br = solve(x + half, y + half, half)
            return Node(False, False, tl, tr, bl, br)

        return solve(0, 0, n)
