from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        # 1.二分法查找
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            # 找到目标值，返回对应的索引
            if target == nums[mid]:
                return mid
            if nums[0] <= nums[mid]:
                # 如果处于区间[0, mid]区间内，则右指针移至中间指针的位置
                # 否则，左指针移动
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


Nums = [4, 5, 6, 7, 0, 1, 2]
Target = 0
print(Solution().search(Nums, Target))
