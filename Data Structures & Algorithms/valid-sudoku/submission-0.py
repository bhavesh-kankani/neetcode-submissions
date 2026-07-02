def isGridValid(board, x, y):
    s = set()
    for i in range(x, x+3):
        for j in range(y, y+3):
            if board[i][j] != "." and board[i][j] in s:
                return False
            else:
                s.add(board[i][j])
    return True
class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            s = set()
            for col in range(9):
                if board[row][col] != "." and board[row][col] in s:
                    return False
                else:
                    s.add(board[row][col])
        print("rows checked")
        for col in range(9):
            s = set()
            for row in range(9):
                if board[row][col] != "." and board[row][col] in s:
                    return False
                else:
                    s.add(board[row][col])
        print("cols checked")
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not isGridValid(board, i, j):
                    return False 
        return True