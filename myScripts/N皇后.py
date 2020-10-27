class Solution(object):
    def __init__(self):
        self.res = []

    def solveNQueens(self, n):
        board = [['.'] * n for _ in range(n)]
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board, row):
        # for i in board:
        #     print(i)
        # 结束条件
        if row == len(board) - 1:
            print('*' * 20)
            print(board)
            self.res.append(board.copy())
            return

        cols = len(board[row])

        for col in range(cols):
            # 排除不合法的选择
            if not self.isValid(board, row, col):
                continue
            # 做选择
            board[row][col] = 'Q'
            # 进行下一次选择
            self.backtrack(board, row + 1)
            # 撤销选择
            board[row][col] = '.'

    def isValid(self, board, row, col):
        n = len(board)
        for i in range(n):
            if board[i][col] == 'Q':
                return False

        for r in range(row - 1):
            for c in range(col - 1):
                if board[r][c] == 'Q':
                    return False

            for c in range(col + 1, len(board[row])):
                if board[r][c] == 'Q':
                    return False

        return True


s = Solution().solveNQueens(8)
print(s)
