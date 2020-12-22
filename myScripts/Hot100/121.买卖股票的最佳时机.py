from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # 从后往前遍历，取最大利益
        n = len(prices)
        max_profit = 0
        max_val = prices[n - 1]
        for i in range(n - 2, -1, -1):
            if max_val < prices[i]:
                max_val = prices[i]
            else:
                max_profit = max(max_profit, max_val - prices[i])
        return max_profit


# Prices = [7, 1, 5, 3, 6, 4]
# Prices = [7, 6, 4, 3, 1]
# Prices = [2, 4, 1]
# Prices = []
print(Solution().maxProfit(Prices))
