from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for am in range(coin, amount + 1):
                dp[am] += dp[am - coin]

        return dp[amount]


Amount = 5
Coins = [1, 2, 5]
# Amount = 3
# Coins = [2]
# Amount = 10
# Coins = [5]
print(Solution().change(Amount, Coins))
