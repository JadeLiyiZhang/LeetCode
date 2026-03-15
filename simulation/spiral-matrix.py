class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        top, bottom = 0, row - 1
        left, right = 0, col - 1
        res = []

        while left <= right and top <= bottom:
            # from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            # from top to bottom
            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1
            # from right to left
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    res.append(matrix[bottom][k])
                bottom -= 1
            # from bottom to top
            if left <= right:
                for m in range(bottom, top - 1, -1):
                    res.append(matrix[m][left])
                left += 1
        
        return res
