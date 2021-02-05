from typing import List


# # 将问题转化为0-1背包问题，使用动态规划求解
# # 时间复杂度：O(NC), 空间复杂度：O(NC), N是元素的个数， C是元素和的一半
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         s, n = 0, len(nums)
#         for num in nums:
#             s += num
#         # 如果累加和为奇数，则无法分割为两个等和子集
#         if s % 2 != 0:
#             return False
#         target = s // 2
#
#         # 状态dp[i][j]表示从数组的[0, i]区间内，能够挑选一些正整数，使得和为j
#         dp = [[False] * (target + 1) for _ in range(n)]
#         # 先填第一行dp的第一行只能让容积大小为自己的数填满
#         # 如果存在某个值大于累加和的一半，则必不可能分割为等和子集
#         if nums[0] <= target:
#             dp[0][nums[0]] = True
#         else:
#             return False
#         # 填其他行
#         for i in range(1, n):
#             for j in range(target + 1):
#                 if nums[i] < j:
#                     # 两种情况
#                     # 1. 选择nums[i]：在[0, i - 1]子区间内找到一部分元素，使得其和为j-nuns[i]
#                     # 2. 不选择nums[i]: 在子区间[0, i - 1]内已经有一部分元素的和为j，则dp[i][j]为True
#                     dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
#                 elif nums[i] == j:
#                     dp[i][j] = True
#                 else:
#                     dp[i][j] = dp[i - 1][j]
#
#         return dp[n - 1][target]

# 空间优化
# 1. 因为当前值只参考了前一行的值，所以可以使用两行的滚动数组优化空间复杂度
# 2. 滚动数组可以进一步的优化，只使用一维的数组，从后往前依次填表
# 时间复杂度：O(NC),空间复杂度O(C)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s, n = 0, len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = [False] * (target + 1)
        dp[0] = True
        if nums[0] <= target:
            dp[nums[0]] = True

        for i in range(1, n):
            # 从后向前 填表过程中，只要nums[i] <= j 不满足，则可以退出循环
            # 因为后面的值会越来越小，没有必要继续做判断
            for j in range(target, nums[i] - 1, -1):
                if dp[target]:
                    return True
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[target]


# Nums = [1, 5, 11, 5]
# Nums = [1, 2, 3, 5]
Nums = [3, 3, 3, 4, 5]
print(Solution().canPartition(Nums))
