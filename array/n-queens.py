class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        chessboard = ['.' * n for _ in range(n)]
        self.backtracking(n, 0, chessboard, result)
        return [[''.join(row) for row in solution] for solution in result]

    def backtracking(self, n, row, chessboard, result):
        if row == n:
            result.append(chessboard[:])
            return

        for col in range(n):
            if self.isValid(row, col, chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]
                self.backtracking(n, row + 1, chessboard, result)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]

    def isValid(self, row, col, chessboard):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False

        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        p = row - 1
        q = col + 1
        while p >= 0 and q < len(chessboard):
            if chessboard[p][q] == 'Q':
                return False
            p -= 1
            q += 1

        return True
