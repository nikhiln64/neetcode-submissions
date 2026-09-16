class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            rowSet = set()
            colSet = set()
            for j in range(len(board[i])):
                rowVal = board[i][j]
                colVal = board[j][i]
                if rowVal != "." and rowVal in rowSet:
                    return False
                rowSet.add(rowVal)
                if colVal != "." and colVal in colSet:
                    return False
                colSet.add(colVal)

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
