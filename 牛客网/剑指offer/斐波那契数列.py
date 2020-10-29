# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # 辅助数组空间
        # dp = [0] * (n + 1)
        # dp[1] = 1
        #
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        #
        # return dp[n]

        # 辅助变量
        pre1, pre2 = 0, 1
        c = 0
        for i in range(2, n+1):
            c = pre1 + pre2
            pre1 = pre2
            pre2 = c

        return c


k = 39
print(Solution().Fibonacci(k))
