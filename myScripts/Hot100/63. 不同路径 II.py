class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 1.自写
        # if obstacleGrid[0][0] == 1:
        #     return 0
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if obstacleGrid[i][j] == 1:
        #             dp[i][j] = 0
        #         else:
        #             if i == 0 and j == 0:
        #                 dp[0][0] = 1
        #             elif i == 0 and j > 0:
        #                 dp[i][j] += dp[i][j - 1]
        #             elif j == 0 and i > 0:
        #                 dp[i][j] += dp[i - 1][j]
        #             else:
        #                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        #         # print(i, j, dp)
        # return dp[-1][-1]

        #题解 2. 滚动数组优化
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [0] * n
        f[0] = 0 if obstacleGrid[0][0] == 1 else 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0
                elif j >= 1 and obstacleGrid[i][j - 1] == 0:
                    f[j] += f[j - 1]

        return f[-1]