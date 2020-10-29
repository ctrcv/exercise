from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 先对envelopes数组进行排序
        # 排序规则为：按envelope[0]升序排序，当envelope[0]相同时，envelope[1]降序排列
        # 最后，根据envelope[1]实现最长递增序列
        if not envelopes:
            return 0

        # 排序
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # 求最长递增子序列长
        # def lis(arr):
        #     n = len(arr)
        #     dp = [1] * n
        #     for i in range(n):
        #         for j in range(i):
        #             if arr[i][1] > arr[j][1]:
        #                 dp[i] = max(dp[i], dp[j] + 1)

        #     return max(dp)

        from bisect import bisect_left
        # bisect 是二分算法模块
        # bisect无法处理倒序数据
        def lis(arr):
            dp = []
            for i in range(len(arr)):
                idx = bisect_left(dp, arr[i][1])
                if idx == len(dp):
                    dp.append(arr[i][1])
                else:
                    dp[idx] = arr[i][1]

            return len(dp)

        return lis(envelopes)


# Envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
Envelopes = [[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]
print(Solution().maxEnvelopes(Envelopes))
