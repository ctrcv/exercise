from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1.贪心算法，时间复杂度O(n),空间O(1)
        # 主要思想：判断当前位置之前的序列元素和是否大于0.
        # 如果大于0，则与当前元素相加，记作当前和curr_sum；如果小于0，则curr_sum直接取当前元素值
        # 对比curr_sum与最大和max_sum，取最大值赋与max_sum
        # curr_sum = max_sum = nums[0]
        # for i, num in enumerate(nums):
        #     if i == 0:
        #         continue
        #     curr_sum = max(curr_sum + num, num)
        #     max_sum = max(max_sum, curr_sum)
        #
        # return max_sum

        # 方法2：动态规划,复杂度同
        # 主要思想：判断原地修改后的nums中当前位置的前一个位置的值是否大于0
        # 如果前一个位置值大于0，则当前位置的新值等于两者之和；否则，当前值保持不变.最后，取数组中的最大值返回
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(max_sum, nums[i])

        return max_sum


Nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(Nums))