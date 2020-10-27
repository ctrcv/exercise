from typing import List


class Solution:
    # 方法1. 常规dp。只求最长上升子序列的长度可用
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        print(dp)
        return max(dp)

    # 方法2：利用贪心+二分法求长度
    # 参考leetcode官方题解

    # 方法2：贪心+二分法。既可求最长上升子序列的长度，又可以得到最长上升子序列
        # 第一步：利用贪心+二分求最长递增子序列长度
    # 参考牛客网
    #     res = []
    #     maxLen = []
    #     if not arr:
    #         return res
    #     res.append(arr[0])
    #     maxLen.append(1)
    #
    #     for i in range(1, len(arr)):
    #         if arr[i] > res[-1]:
    #             res.append(arr[i])
    #             maxLen.append(len(res))
    #         else:
    #             pos = self.lower_bound(res, arr[i])
    #             res[pos] = arr[i]
    #             maxLen.append(pos + 1)
    #
    #     # 第二步：填充最长递增子序列
    #     j, k = len(arr) - 1, len(res)
    #     while k > 0:
    #         if maxLen[j] == k:
    #             k -= 1
    #             res[k] = arr[j]
    #
    #         j -= 1
    #
    #     return res
    #
    # def lower_bound(self, arr, val):
    #     # 返回有序数组arr中第一个比val大的值的索引
    #     for i, a in enumerate(arr):
    #         if a >= val:
    #             return i
    #     return -1


# arr = [10, 9, 2, 5, 3, 4, 7, 101, 18, 19]
arr = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(Solution().lengthOfLIS(arr))
