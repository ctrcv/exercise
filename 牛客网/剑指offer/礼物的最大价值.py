from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 方法1，回溯，超时
        # if not grid:
        #     return -1
        # global res
        # res = -1
        # m, n = len(grid), len(grid[0])
        # # print(m, n)
        #
        # def dfs(i, j, val):
        #     if i == m - 1 and j == n - 1:
        #         global res
        #         res = max(res, val)
        #         return
        #
        #     if i + 1 < m:
        #         dfs(i + 1, j, val + grid[i + 1][j])
        #     if j + 1 < n:
        #         dfs(i, j + 1, val + grid[i][j + 1])
        #
        # dfs(0, 0, grid[0][0])
        # return res

        # 方法1，简化
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i >= m or j >= n:


        # 优化方法1
        # 方法2， 动态规划，
        # if not grid:
        #     return 0
        # m, n = len(grid), len(grid[0])
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        #
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i-1][j-1]
        #
        # return dp[m][n]

        # 方法2优化
        # 方法3,空间优化
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[j] = max(dp[j], dp[j - 1]) + grid[i - 1][j - 1]

        return dp[n]


# grd = [[1, 3, 1],
#        [1, 5, 1],
#        [4, 2, 1]]
grd = [[7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5], [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
       [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8], [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
       [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4], [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
       [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4], [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
       [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3], [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
       [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7], [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9]]
print(Solution().maxValue(grd))
