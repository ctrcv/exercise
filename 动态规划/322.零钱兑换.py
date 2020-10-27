from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0 or not coins:
            return -1

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         # if i - coin >= 0:
        #         #     dp[i] = min(dp[i - coin] + 1, dp[i])
        #
        #         if i < coin: continue
        #         dp[i] = min(dp[i - coin] + 1, dp[i])
        #
        #         # if i - coin > 0:
        #         #     dp[i] = min(dp[i - coin] + 1, dp[i])
        #         # elif i == coin:
        #         #     dp[i] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i - coin] + 1, dp[i])

        return -1 if dp[-1] == amount + 1 else dp[-1]

# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         count = 0
#         target = 1 << amount  # 最左端的 1 代表 0
#         while target:
#             if target & 1:
#                 return count
#             aux = target
#             for x in coins:
#                 if x <= amount:
#                     target |= aux >> x
#             count += 1
#             if target == aux:
#                 return -1


Coins = [1, 2, 5]
Amount = 11
# Coins = [2]
# Amount = 3
# Amount = 0
# Coins = [1]
# Amount = 2
print(Solution().coinChange(Coins, Amount))
