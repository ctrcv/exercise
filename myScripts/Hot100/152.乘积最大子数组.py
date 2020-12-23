from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # 动态规划
        # 用两个数组分别记录最大、最小子数组乘积值
        # 当num[i] > 0时，当前位置子数组乘积的最大值等于前面子数组乘积最大值乘num[i]，结果与num[i]对比取最大值
        # 当num[i] <= 0时，当前位置子数组乘积的最大值等于子数组乘积最小值乘以num[i]，结果与num[i]比较取最大值
        # maxn = [0] * n
        # minn = [0] * n
        # maxn[0] = minn[0] = nums[0]
        # for i in range(1, n):
        #     if nums[i] > 0:
        #         maxn[i] = max(maxn[i - 1] * nums[i], nums[i])
        #         minn[i] = min(minn[i - 1] * nums[i], nums[i])
        #     else:
        #         maxn[i] = max(minn[i - 1] * nums[i], nums[i])
        #         minn[i] = min(maxn[i - 1] * nums[i], nums[i])
        #
        # return max(maxn)

        # 空间优化
        # maxn[i] 和 minn[i]的取值只取决于 maxn[i-1] 和 minn[i - 1]，minn也相同， 没必要申请O(n)的数组空间
        ans = maxn = minn = nums[0]
        for i in range(1, n):
            # 需要两个临时变量存储上一对值，防止max或min中的最大最小值不是上一对的数值
            mx, mn = maxn, minn
            # if nums[i] > 0:
            #     maxn = max(mx * nums[i], nums[i])
            #     minn = min(mn * nums[i], nums[i])
            # else:
            #     maxn = max(mn * nums[i], nums[i])
            #     minn = min(mx * nums[i], nums[i])
            # ans = max(maxn, ans)

            # 或者不用判断num[i]的正负性，直接每次对比取出最大最小值
            maxn = max(mx * nums[i], mn * nums[i], nums[i])
            minn = min(mx * nums[i], mn * nums[i], nums[i])
            ans = max(maxn, ans)
        return ans


Nums = [2, 3, -2, 4]
# Nums = [-2, 0, -1]
# Nums = [-3, -1, -1]
# Nums = [-2, 3, -4]
# Nums = [-4,-3,-2]
print(Solution().maxProduct(Nums))
