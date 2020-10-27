class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    # 设定 fi 表示前 i 个物品装入大小为 j 的背包里, 可以获取的最大价值总和.
    # 决策就是第i个物品装不装入背包, 所以状态转移方程就是
    # f[i][j] = max(f[i - 1][j], f[i - 1][j - A[i]] + V[i])
    # def backPackII(self, m, A, V):
    #     # write your code here
    #     n = len(A)
    #     dp = [[0] * (m + 1) for _ in range(n + 1)]
    #     for i in range(n + 1):
    #         for j in range(m + 1):
    #             if i == 0 or j == 0:
    #                 dp[i][j] = 0
    #             elif A[i - 1] > j:
    #                 dp[i][j] = dp[i - 1][j]
    #             else:
    #                 dp[i][j] = max(dp[i - 1][j - A[i - 1]] + V[i - 1], dp[i - 1][j])
    #     return dp[-1][-1]

    # 使用滚动数组优化
    def backPackII(self, m, A, V):
        dp = [0] * (m + 1)
        n = len(A)
        for i in range(n):
            for j in range(m, A[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - A[i]] + V[i])

        return dp[m]



m1 = 10
A1 = [2, 3, 5, 7]
V1 = [1, 5, 2, 4]

print(Solution().backPackII(m1, A1, V1))
