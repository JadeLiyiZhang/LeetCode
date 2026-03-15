class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        # Transpose the matrix (swap matrix[i][j] with matrix[j][i])
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)

        # Reverse each row (swap matrix[i][j] with matrix[i][n - j - 1])
        for row in matrix:
            row.reverse()
        return matrix