# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # a, b = 1, 1
        # s = 0
        #
        # for _ in range(0, number):
        #     c = a + b
        #     a = b
        #     b = c
        #     s += b
        # print(s)
        # return b
        if number == 1 or number == 0:
            return 1

        # 方法1：暴力求解
        # f[n] = f[n-1] + f[n-2] + ... + f[0]
        # dp = [0] * (number + 1)
        # dp[0], dp[1] = 1, 1
        #
        # for i in range(2, number+1):
        #     for j in range(i):
        #         dp[i] += dp[j]
        #
        # return dp[number]

        # 方法2：优化
        # f[n] = f[n - 1] + f[n - 2] + ... + f[0]
        # f[n - 1] = f[n-2] + f[n-3] + ... + f[0]
        # f[n] = f[n-1]*2

        a, b = 1, 1
        for i in range(2, number + 1):
            b = a << 1
            # b = a * 2
            a = b
        return b


n = 4
print(Solution().jumpFloorII(n))
