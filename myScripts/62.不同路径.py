class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


# M, N = 3, 7  # 28
# M, N = 3, 3  # 6
M, N = 3, 2  # 6
print(Solution().uniquePaths(M, N))
