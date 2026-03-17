class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        table = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j] == 1:
                    if i - 1 >= 0 and j - 1 >= 0:
                        table[i - 1][j - 1] += 1
                    if i - 1 >= 0:
                        table[i - 1][j] += 1
                    if i - 1 >= 0 and j + 1 < col:
                        table[i - 1][j + 1] += 1
                    if j - 1 >= 0:
                        table[i][j - 1] += 1
                    if j + 1 < col:
                        table[i][j + 1] += 1
                    if i + 1 < row and j - 1 >= 0:
                        table[i + 1][j - 1] += 1
                    if i + 1 < row:
                        table[i + 1][j] += 1
                    if i + 1 < row and j + 1 < col:
                        table[i + 1][j + 1] += 1
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 1:
                    if table[i][j] < 2 or table[i][j] > 3:
                        board[i][j] = 0
                elif board[i][j] == 0 and table[i][j] == 3:
                    board[i][j] = 1
