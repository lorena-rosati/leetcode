class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row, col, square = defaultdict(list), defaultdict(list), defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in square[(i//3, j//3)]):
                    return False
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                square[(i//3, j//3)].append(board[i][j])
        return True