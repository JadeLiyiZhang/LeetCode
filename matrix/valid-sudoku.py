class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            table = set()
            for col in range(9):
                if board[row][col] != '.' and board[row][col] in table:
                    return False
                else:
                    table.add(board[row][col])
        
        for col in range(9):
            table = set()
            for row in range(9):
                if board[row][col] != '.' and board[row][col] in table:
                    return False
                else:
                    table.add(board[row][col])
        
        boxes = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                idx = (row // 3) * 3 + (col // 3)
                if board[row][col] in boxes[idx] and board[row][col] != '.':
                    return False
                else:
                    boxes[idx].add(board[row][col])

        return True