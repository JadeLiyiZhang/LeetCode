class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'S'
                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for i in range(len(board)):
            for j in [0, cols - 1]:
                if board[i][j] == 'O':
                    dfs(i, j)

        for i in [0, rows - 1]:
            for j in range(cols):
                if board[i][j] == 'O':
                    dfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
