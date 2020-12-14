from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        return self.search(nums, 0, len(nums) - 1, target)

    def search(self, nums, left, right, target):
        if left > right:
            return [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if nums[left] != target:
                    left = self.search(nums, left + 1, mid, target)[0]
                if nums[right] != target:
                    right = self.search(nums, mid, right - 1, target)[1]
                return [left, right]

        return [-1, -1]


Nums = [5, 7, 7, 8, 8, 10]
Target = 6
# Nums = [5, 7, 7, 8, 8, 10]
# Target = 8
print(Solution().searchRange(Nums, Target))
