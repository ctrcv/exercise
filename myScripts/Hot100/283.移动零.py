from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        # 1. 两次次遍历
        # 第一次遍历统计数组中0的个数
        # j, n = 0, len(nums)
        #
        # for i in range(n):
        #     # 用非零元素将零元素原位置覆盖掉
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         j += 1
        # # j之前位置的元素因都被非零值覆盖，所以j位置后的元素全部赋值为0即可
        # for i in range(j, n):
        #     nums[i] = 0

        # 2. 一次遍历，快排思想，双指针.时间复杂度O(n)，空间O(1)
        # 将非零元素移到左边,零移到右边
        # 当数组中存在0的时候，左指针记录值为0的左索引
        # 不存在0的时候，索引i等于左指针left

        left = 0
        for i, num in enumerate(nums):
            # 如果元素不为零，索引i和左指针一起向右移，并将对应元素位置互换
            if num != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
