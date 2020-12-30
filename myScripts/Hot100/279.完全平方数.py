import math

# 官方题解：暴力、递归、动态规划、BFS、数学法
# 方法：动态规划
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        # 最坏情况：该数只能由1累加得到
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(int(math.sqrt(i)), 1, -1):
                # 平方数不会大于i的开根值
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]
