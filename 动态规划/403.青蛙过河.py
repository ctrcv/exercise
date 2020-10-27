from typing import List


class Solution:
    # 参考官方题解
    # 1. 暴力递归
    # def canCross(self, stones: List[int]) -> bool:
    #     return self._canCross(stones, 0, 0)
    #
    # def _canCross(self, stones, ind, jumpsize):
    #     for i in range(ind + 1, len(stones)):
    #         # 检查间隔
    #         gap = stones[i] - stones[ind]
    #         if jumpsize - 1 <= gap <= jumpsize + 1:
    #             if self._canCross(stones, i, gap):
    #                 return True
    #
    #     return ind == len(stones) - 1

    # 2. 暴力递归二分法优化
    # 3. 记忆化搜索
    # def canCross(self, stones: List[int]) -> bool:
    #     n = len(stones)
    #     memo = [[-1] * n for _ in range(n)]
    #     return self._canCross(stones, memo, 0, 0) == 1
    #
    # def _canCross(self, stones, memo, ind, jumpsize):
    #     if memo[ind][jumpsize] != -1:
    #         return memo[ind][jumpsize]
    #     for i in range(ind + 1, len(stones)):
    #         gap = stones[i] - stones[ind]
    #         if jumpsize - 1 <= gap <= jumpsize + 1:
    #             if self._canCross(stones, memo, i, gap) == 1:
    #                 memo[ind][gap] = 1
    #                 return 1
    #
    #     memo[ind][jumpsize] = 1 if ind == len(stones) else 0
    #     return memo[ind][jumpsize]

    # 4.记忆化 + 二分
    # 5.动态规划 + 哈希表
    # def canCross(self, stones: List[int]) -> bool:
    #     record = {}
    #     for i in stones:
    #         record[i] = record.get(i, set())
    #
    #     record[0].add(0)
    #     for s in stones:
    #         for k in record[s]:
    #             for step in [k - 1, k, k + 1]:
    #                 if step > 0 and record[s + step] in record:
    #                     record[s + step].add(step)
    #
    #     return len(record[stones[-1]]) > 0

    # 6.动态规划
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False] * (n + 1) for _ in range(n)]
        dp[0][0] = True
        # dp的长度之所以定义为len+1是因为第0块石头为0步，就算每跳一次加一步，最多也只能跳len步
        # dp[i][k]表示能否从第i个石头前面的任意一个石头j用k步跳到第i个石头
        for i in range(1, n):
            for j in range(i):
                k = stones[i] - stones[j]
                if k < n and k <= stones[j] + 1:
                    dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                    if i == n - 1 and dp[i][k]:
                        return True

        return False


Stones = [0, 1, 3, 5, 6, 8, 12, 17]  # True
# Stones = [0, 1, 3, 6, 10, 13, 14]
print(Solution().canCross(Stones))
