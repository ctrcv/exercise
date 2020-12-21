class Solution:
    def climbStairs(self, n: int) -> int:
        # 方法：动态规划
        # if n < 3: return n
        # dp = [0] * (n + 1)
        # dp[0], dp[1] = 1, 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[-1]

        # 空间优化
        if n < 3: return n
        a, b = 1, 2
        for i in range(3, n + 1):
            c = a + b
            a, b = b, c
        return c


N = 3
print(Solution().climbStairs(N))
