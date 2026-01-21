class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, index, seen):
            if index == len(word):
                return True
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[index] and (x, y) not in seen:
                seen.add((x, y))
                if dfs(x + 1, y, index + 1, seen) or dfs(x - 1, y, index + 1, seen) or dfs(x, y - 1, index + 1, seen) or dfs(x, y + 1, index + 1, seen):
                    return True
                seen.remove((x, y))
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True

        return False
