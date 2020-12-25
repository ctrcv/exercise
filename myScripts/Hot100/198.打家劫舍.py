from typing import List


# 动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return nums[-1]
        # dp = [0] * (n + 1)
        # dp[0], dp[1] = 0, nums[0]  # 需要设一个值为0的头节点
        # for i in range(2, n + 1):
        #     # 对于当前位置，只有偷与不偷两种状态
        #     # 取决于截止至上一个房子偷盗的数额与截止至上上个房子与当前房子数额和
        #     # 如果大于，则抢劫；小于则不抢劫
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        # return dp[-1]

        # 空间优化
        # dp[i]只与dp[i-1和dp[i-2]有关
        pre = curr = 0
        for num in nums:
            pre, curr = curr, max(curr, pre + num)
        return curr


# Nums = [1,2,3,1]
# Nums = [2, 7, 9, 3, 1]
Nums = [2, 1, 1, 2]
print(Solution().rob(Nums))
