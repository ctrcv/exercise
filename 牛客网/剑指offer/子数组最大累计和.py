from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 参考：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solution/mian-shi-ti-42-lian-xu-zi-shu-zu-de-zui-da-he-do-2/
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i], 0)
        # print(nums)
        return max(nums)


numbers = [1, -2, 3, 5, -2, 6, -1]
# numbers = [-2, 1]
print(Solution().maxSubArray(numbers))
