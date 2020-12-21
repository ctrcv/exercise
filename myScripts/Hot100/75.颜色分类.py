from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swqp(nums, idx1, idx2):
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

        # 方法1. 使用快速排序中的partition思想，即
        # all in [0, zero) = 0
        # all in [zero, i) = 1
        # all in [two, len - 1] = 2
        # 时间复杂度：O(N)
        if len(nums) < 2: return
        i, zero, two = 0, 0, len(nums)
        while i < two:
            if nums[i] == 0:
                # 当值等于0时，交换i和zero的对应元素的值，然后i和zero都向右移
                swqp(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                # 当值等于1时，i指针右移，其余指针保持
                i += 1
            else:
                # 当值等于2时，因为two初始设置为nums的长度，直接处理会越界，需要先左移
                two -= 1
                swqp(nums, i, two)

        print(nums)


Nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(Nums)
