from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 二分法,时间复杂度O(nlogn), 空间O(1)
        # 要点:
        # 1. 数组中的数字大小区间[1,n], 共包含n+1个数字
        # 2.对于nums中的一个数i,如果小于等于i的数字个数cnt等于i,说明数字i之前的数字都没有重复的
        # 3.当i之前的数字统计cnt大于i,则说明i之前存在重复的数字,缩短指针范围,继续二分搜索
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2  # 取中间值
            cnt = 0  # 统计数字mid前的个数
            for num in nums:
                # 注意=号
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                # 区间[left, mid]中不存在重复的数字,left指针右移
                left = mid + 1
            else:
                # 有重复的数字,右指针左移
                right = mid

        return left


Nums = [1, 3, 4, 2, 2]
print(Solution().findDuplicate(Nums))
