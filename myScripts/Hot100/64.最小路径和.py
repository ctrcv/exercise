from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 方法1. 动态规划
        # 当前位置最小值只与同行前一列或同列前一行的元素的最小值相关
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return int(dp[-1][-1])

        # 优化：如题62相同，空间复杂度可以优化，例如每次只存储上一行的 \textit{dp}dp 值，则可以将空间复杂度优化到 O(n)O(n)。


Grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().minPathSum(Grid))
