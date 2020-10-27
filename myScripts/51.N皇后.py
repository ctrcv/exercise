from typing import List

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         def generateBoard():
#             board = list()
#             for i in range(n):
#                 row[queens[i]] = "Q"
#                 board.append("".join(row))
#                 row[queens[i]] = "."
#             return board
#
#         def backtrack(row: int):
#             if row == n:
#                 board = generateBoard()
#                 solutions.append(board)
#             else:
#                 for i in range(n):
#                     if i in columns or row - i in diagonal1 or row + i in diagonal2:
#                         continue
#                     queens[row] = i
#                     columns.add(i)
#                     diagonal1.add(row - i)
#                     diagonal2.add(row + i)
#                     backtrack(row + 1)
#                     columns.remove(i)
#                     diagonal1.remove(row - i)
#                     diagonal2.remove(row + i)
#
#         solutions = list()
#         queens = [-1] * n
#         columns = set()
#         diagonal1 = set()
#         diagonal2 = set()
#         row = ["."] * n
#         backtrack(0)
#         return solutions

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        res = []

        def backtrack(board, row):
            if row == n:
                bod = compressBoard(board)
                res.append(bod)
                return

            for col in range(n):
                if not isvalid(row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'

        def isvalid(row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            i, j = row - 1, col - 1  # 左上
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, col + 1  # 右下
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def compressBoard(board):
            boad = []
            for i in range(n):
                boad.append(''.join(board[i]))
            return boad

        backtrack(board, 0)
        return res



N = 8
res = Solution().solveNQueens(N)
print(res)
