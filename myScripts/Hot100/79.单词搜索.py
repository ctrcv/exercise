from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        used = [[False] * n for _ in range(m)]

        def dfs(i, j, k):
            if i == m and j == n:
                return False
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            if not used[i][j]:
                used[i][j] = True
                ret1, ret2 = False, False
                if 0 <= i < n and 0 <= j < n and k < len(word)  - 2:
                    ret1 = dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1)
                if i > 0 and j > 0 and k < len(word) - 2:
                    ret2 = dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1)
                used[i][j] = False
                return ret1 or ret2


        return dfs(0, 0, 0)


Board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]
Word = "ABCCED"
print(Solution().exist(Board, Word))
# Solution().exist(Board, Word)
