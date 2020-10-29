# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2

        # 0. 暴力递归，时间复杂度 O(number!)， 空间复杂度 O(number)
        # def backtrack(n):
        #     if n <= 4:
        #         return n
        #
        #     ret = -1
        #     for i in range(1, n):
        #         ret = max(ret, i * backtrack(n - i))
        #
        #     return ret
        #
        # return backtrack(number)

        # 1. 动态规划_迭代版本, 自下向上  时间复杂度 O(number ^ 2)， 空间复杂度 O(number)
        # dp = [0] * (number + 1)
        # dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
        #
        # for i in range(4, number + 1):
        #     for j in range(1, i // 2 + 1):
        #         dp[i] = max(dp[i], dp[j] * dp[i - j])
        #
        # return dp[number]

        # 2. 动态规划_递归版本，自上向下
        # mark = [-1] * (number + 1)
        #
        # def backtrack(n):
        #     if n <= 4:
        #         return n
        #
        #     if mark[n] > 0:
        #         return mark[n]
        #
        #     ret = -1
        #     for i in range(1, n):
        #         ret = max(ret, i * backtrack(n - i))
        #
        #     mark[n] = ret
        #     return ret
        #
        # return backtrack(number)

        # 3. 贪婪算法
        # 尽可能多地剪去长度为3的绳子段
        timesOf3 = number // 3

        # 当绳子最后剩下的绳子长度为4时，不能再剪去绳子长度为3的绳子段
        # 更好的办法是绳子剪成长度为2的两段，因为2×2 > 1×3
        if number - timesOf3 * 3 == 1:
            timesOf3 -= 1

        timesOf2 = (number - 3 * timesOf3) // 2
        ret = pow(3, timesOf3) * pow(2, timesOf2)
        return int(ret)


# 10 ：36
# 8 ：18
res = Solution().cutRope(10)
print(res)
