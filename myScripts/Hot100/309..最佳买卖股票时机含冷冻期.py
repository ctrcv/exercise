from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 设f[i]为第i天的收益
        # 情况1:表示目前持有一支股票,累计收益为f[i][0]
        # 情况2:表示当前没有持有股票,且第i天结束后处于冷冻期
        # 情况3:表示当前没有持有股票,且第i天结束后不处于冷冻期

        # 对于f[i][0],目前持有的股票可以使第i-1天持有的,对应的状态为f[i-1][0],
        # 或者是第i天买入的,这种情况则要求dii-1天后不处于冷冻期,即第i-1天的状态需要是f[i-1][2]
        # 则f[i][0]=max(f[i-1][0], f[i-1][2] - price[i])

        # 对于f[i][1],表示第i天将股票卖出,则要求第i-1持有股票
        # f[i][1]=f[i-1][0]+prices[i]

        # 对于f[i][2],则表示不做任何操作,第i-1天要么处于无股票冷冻期f[i-1][1]或f[i-1][2]
        # f[i][2]=max(f[i-1][1], f[i-1][2])

        # 最终受益应该为:max(f[n-1][1],f[n-1][2]),因为第n天持有股票是无意义的,因此不将f[n][0]考虑进来
        # maxProfix = max(f[n-1][1], f[n-1][2])

        # 1. 动态规划
        # if not prices: return 0
        # n = len(prices)
        # f = [[0] * 3 for _ in range(n)]
        # f[0][0] = - prices[0]
        # f[0][1] = 0
        # f[0][2] = 0
        # for i in range(1, n):
        #     f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
        #     f[i][1] = f[i - 1][0] + prices[i]
        #     f[i][2] = max(f[i - 1][1], f[i - 1][2])
        #
        # return max(f[n - 1][1], f[n - 1][2])

        # 方法1空间优化
        # f[i][]只与f[i-][]有关
        if not prices: return 0
        f0, f1, f2 = - prices[0], 0, 0
        for i in range(1, len(prices)):
            newf0 = max(f0, f2 - prices[i])
            newf1 = f0 + prices[i]
            newf2 = max(f1, f2)
            f0, f1, f2 = newf0, newf1, newf2

        return max(f1, f2)


Prices = [1, 2, 3, 0, 2]
print(Solution().maxProfit(Prices))
