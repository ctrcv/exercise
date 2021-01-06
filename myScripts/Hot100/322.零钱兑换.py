from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0: return -1

        # 1.动态规划
        # dp数组初始值设置为amount+1,因为最坏情况下全由1凑成,最多只需要amount个币,因此amount+1此时则可理解为无穷多个
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         # 如果相等,只需一枚硬币
        #         if i == coin:
        #             dp[i] = 1
        #         # 面值比coin大,则最少的硬币数为当前状态历史的可凑齐的硬币数与dp[i - coin]+1中的最小值
        #         elif i - coin > 0:
        #             dp[i] = min(dp[i], dp[i - coin] + 1)
        #         # 否则,当前硬不能凑
        #         elif i < coin:
        #             continue
        #
        # return dp[-1] if dp[-1] != amount + 1 else -1

        # 调换循环顺序可简化代码
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i - coin] + 1, dp[i])

        return -1 if dp[-1] == amount + 1 else dp[-1]


# Coins = [1, 2, 5]
# Amount = 11
# Coins = [2]
# Amount = 3
Coins = [1]
Amount = 1
print(Solution().coinChange(Coins, Amount))
