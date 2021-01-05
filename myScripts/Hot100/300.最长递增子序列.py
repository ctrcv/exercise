from typing import List


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # 1.动态规划, 时间复杂度O(N^2),空间O(N)
#         # 思想:
#         # 状态dp[i]表示在i位置前的最长递增数组
#         # 对于区间[0, i]中的j,如果nums[i]大于nums[j],则表示nums[i]可以接到nums[j]后形成一个递增序列
#         # 否则,忽略当前位置,移动指针
#         # 最后查找dp数组中的最大值即为最长递增子序列
#         # 状态转移方程为dp[i] = max(dp[i], dp[j] + 1)
#         if not nums: return 0
#         n = len(nums)
#         dp = [1] * n
#         # max_len = 1
#         for i in range(1, n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     # max_len = max(max_len, dp[i])
#         # return max_len
#         return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        # 2. 动态规划+二分查找,时间复杂度:O(nlogn), 空间复杂度O(n)
        # 思想:
        # 定义一个辅助数组tails,tails[k]表示长度为k+1的序列的尾部元素
        # 设res为tails当前长度,表示当前最长递增子序列的长度
        # 设在区间[0,res]中的j,考虑每轮遍历nums[k]时,通过二分法遍历[0,res)列表区间,找出nnum[k]大小分界点
        # 会有两种情况:
        # 1. 区间中存在tails[i]>nums[k],将第一个满足tails[i] > num[k]执行tails[i] = nums[k];
        # 因为更小的值在后面可能更容易出现比其大的值
        # 2.区间中不存在tails[i]>nums[k],意味着nums[k]比tails中的任意元素都大,可以直接接入序列中,新子序列的长度为res + 1
        n = len(nums)
        tails, res = [0] * n, 0
        for num in nums:
            left, right = 0, res
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = num
            if right == res:
                res += 1
        return res


Nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Nums = [0, 1, 0, 3, 2, 3]
# Nums = [7, 7, 7, 7, 7, 7]
print(Solution().lengthOfLIS(Nums))
