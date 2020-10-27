from typing import List


class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     if m == 0 and n == 0:
    #         return 0
    #
    #     dp = [[float('inf')] * (n) for _ in range(m)]
    #     for i in range(m):
    #         for j in range(n):
    #             if i == 0 and j == 0:
    #                 dp[i][j] = grid[i][j]
    #             else:
    #                 dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    #
    #     return dp[m-1][n-1]

    def minPathSum(self, grid):
        dp = [float('inf')] * (len(grid[0]) + 1)
        dp[1] = 0
        for row in grid:
            for idx, num in enumerate(row):
                dp[idx + 1] = min(dp[idx], dp[idx + 1]) + num
        return dp[-1]


nums = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]
print(Solution().minPathSum(nums))
