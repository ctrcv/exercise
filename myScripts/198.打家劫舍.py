class Solution(object):
    def rob(self, nums: list) -> int:
        # 动态规划
        #
        if not nums: return 0

        # 优化前
        # N = len(nums)
        # dp = [0] * (N + 1)
        # dp[i] = x 表示从第i个房间开始抢劫，最多能抢到的钱为x
        # dp[0] = 0
        # dp[1] = nums[0]
        # for i in range(2, N + 1):
        #     dp[i] = max(dp[i - 1], nums[i -1] + dp[i -2])
        # return dp[N]

        # 空间优化后
        # N = len(nums)
        prev, curr = 0, 0
        for i in nums:
            prev, curr = curr, max(curr, prev + i)

        return curr


nums = [2, 7, 9, 3, 1]
res = Solution().rob(nums)
print(res)
