from typing import List


# # 递归
# class Solution:
#     res = 0
#
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         if not nums:
#             return 0
#
#         n = len(nums)
#
#         # 方法1：自写，超时
#         # def dfs(i, eq):
#         #     if i == n:
#         #         if eval(eq) == S:
#         #             self.res += 1
#         #         return
#         #
#         #     tmp = eq + "+" + str(nums[i])
#         #     dfs(i + 1, tmp)
#         #
#         #     tmp = eq + "-" + str(nums[i])
#         #     dfs(i + 1, tmp)
#         #
#         # dfs(0, "")
#         # return self.res
#
#         # 方法2：方法1简化版，也超时，但运行速度远比方法1快
#         # 时间复杂度O(2^N),空间复杂度O(N), N为数组长度
#         def dfs(i, val):
#             if i == n:
#                 if val == S:
#                     self.res += 1
#                 return
#             dfs(i + 1, val + nums[i])
#             dfs(i + 1, val - nums[i])
#
#         dfs(0, 0)
#         return self.res

# 动态规划
#  找到nums一个正子集和一个负子集，使得总和等于target，与416.分割等和子集的思想类似
# 将问题当成背包问题，使用动态规划求解
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:




# Nums = [1, 1, 1, 1, 1]
# s = 3
Nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
s = 1
print(Solution().findTargetSumWays(Nums, s))
