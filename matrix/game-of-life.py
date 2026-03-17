class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(row):
            for j in range(col):
                neighbors = 0
                for x, y in directions:
                    ni, nj = i + x, j + y
                    if 0 <= ni < row and 0 <= nj < col and abs(board[ni][nj]) == 1:
                        neighbors += 1
                if board[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and neighbors == 3:
                    board[i][j] = 2

        
        for i in range(row):
            for j in range(col):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0