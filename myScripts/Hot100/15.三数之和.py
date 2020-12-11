from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. 暴力算法，时间复杂度O(n^3)
        # 2. 双指针法，O(n^2)
        n = len(nums)
        if n < 3:
            return []
        # 先对nums排序
        nums.sort()
        res = []
        # 设置三指针遍历求和
        # 第一个指针
        for i in range(n):
            # 因为nums是排序后的序列，如果nums[i] > 0，则表示后面的任意序列和都不可能等于0
            # 直接返回
            if nums[i] > 0:
                return res
            # 对于重复的元素，直接跳过，避免出现重复解
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 剩余的两个指针
            left, right = i + 1, n - 1
            while left < right:
                t = nums[i] + nums[left] + nums[right]
                if t == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 去除重复解
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                # 当t < 0,表示left指针所对应的元素值太小，需要往右移动
                elif t < 0:
                    left += 1
                # 不然，right指针左移
                else:
                    right -= 1

        return res


Nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(Nums))
