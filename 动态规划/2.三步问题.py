class Solution:
    def f3(self, n):
        if n < 0:
            return 0
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 4

        # dp = [0] * (n+1)
        # dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 4
        # for i in range(4, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        #
        # return dp[-1] % 1000000007

        a, b, c = 1, 2, 4
        for i in range(4, n + 1):
            a = a + b + c
            a, b, c = b, c, a

        return c % 1000000007


    def f2(self, n):
        if n <= 0:
            return 0
        if n == 1: return 1
        if n == 2: return 2

        a, b = 1, 2
        for i in range(3, n + 1):
            a = a + b
            a, b = b, a

        return b


N = 3
print(Solution().f2(N))
