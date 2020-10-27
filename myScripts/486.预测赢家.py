import time


class Solution(object):
    def PredictTheWinner(self, nums: list) -> bool:
        # 方法1：递归  time cost: 0.2703135013580322
        # def helper(i, j):
        #     if i == j:
        #         return nums[i]
        #     picki = nums[i] - helper(i + 1, j)
        #     pickj = nums[j] - helper(i, j - 1)
        #     return max(picki, pickj)
        #
        #
        # return helper(0, len(nums) - 1) >= 0

        # 方法2：记忆化递归  time cost:0.0009658336639404297
        # n = len(nums)
        # memo = [[0 for _ in range(n)] for _ in range(n)]
        #
        # def helper(i, j):
        #     if memo[i][j] != 0:
        #         return memo[i][j]
        #     if i == j:
        #         memo[i][i] = nums[i]
        #         return nums[i]
        #     picki = nums[i] - helper(i + 1, j)
        #     pickj = nums[j] - helper(i, j - 1)
        #     memo[i][j] = max(picki, pickj)
        #     return memo[i][j]
        #
        # return helper(0, n - 1) >= 0

        # 方法3：动态规划，二维数组 time cost:0.0
        # n = len(nums)
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = nums[i]
        #
        # for i in range(n - 2, -1, -1):
        #     for j in range(i + 1, n):
        #         picki = nums[i] - dp[i + 1][j]
        #         pickj = nums[j] - dp[i][j - 1]
        #         dp[i][j] = max(picki, pickj)
        #
        # return dp[0][n - 1] >= 0

        # 方法4：动态规划，一维数组
        # dp[i][j] 只与dp[i+1][j]和dp[i][j-1]相关
        n = len(nums)
        dp = [nums[i] for i in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[n - 1] >= 0


# n = [1, 5, 233, 7] * 5
n = [1, 5, 2] * 5
t1 = time.time()
s = Solution().PredictTheWinner(n)
t2 = time.time()
print(t2 - t1)
print(s)
