class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def canPlace(row, col, dirX, dirY, i):
            while i < len(word):
                if row < 0 or row >= m or col < 0 or col >= n or board[row][col] == '#' or (board[row][col] != ' ' and board[row][col] != word[i]):
                    return False

                row = row + dirX
                col = col + dirY
                i += 1

            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] == '#':
                return True
            return False

        for i in range(m):
            for j in range(n):
                if (i - 1 < 0 or board[i - 1][j] == '#') and board[i][j] != '#':
                    if canPlace(i, j, 1, 0, 0):
                        return True

                if (i + 1 >= m or board[i + 1][j] == '#') and board[i][j] != '#':
                    if canPlace(i, j, -1, 0, 0):
                        return True

                if (j - 1 < 0 or board[i][j - 1] == '#') and board[i][j] != '#':
                    if canPlace(i, j, 0, 1, 0):
                        return True

                if (j + 1 >= n or board[i][j + 1] == '#') and board[i][j] != '#':   
                    if canPlace(i, j, 0, -1, 0):
                        return True
        
        return False