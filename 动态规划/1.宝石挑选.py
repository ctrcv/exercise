# def solution(arr):
#     maxval = float('-inf')
#     n = len(arr)
#
#     for i in range(n - 1, -1, -1):
#         s = 0
#         for j in range(i, -1, -1):
#             s += arr[j]
#             maxval = max(maxval, s)
#
#     return maxval
#
#
# numbers = [-2, -1]
# numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# numbers = [1, -2, 3, 5, -2, 6, -1, ]

# print(solution(numbers))

from typing import List


class Solution:
    # 暴力法：超时
    # def maxSubArray(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     maxval = float('inf')
    #     n = len(nums)
    #     for i in range(n - 1, -1, -1):
    #         s = 0
    #         for j in range(i, -1, -1):
    #             s += nums[j]
    #             maxval = max(maxval, s)
    #
    #     return maxval

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
            # nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)


# numbers = [-2, -1]
# numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
numbers = [1, -2, 3, 5, -2, 6, -1, ]
print(Solution().maxSubArray(numbers))
