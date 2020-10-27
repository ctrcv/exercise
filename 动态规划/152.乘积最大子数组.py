from typing import List


class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     n = len(nums)
    #     maxn = [0] * n
    #     minn = [0] * n
    #     maxn[0] = minn[0] = nums[0]
    #     for i in range(1, n):
    #         if nums[i] > 0:
    #             maxn[i] = max(maxn[i - 1] * nums[i], nums[i])
    #             minn[i] = min(minn[i - 1] * nums[i], nums[i])
    #         else:
    #             maxn[i] = max(minn[i - 1] * nums[i], nums[i])
    #             minn[i] = min(maxn[i - 1] * nums[i], nums[i])
    #
    #     return max(maxn)

    # def maxProduct(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     maxn = [0] * n
    #     minn = [0] * n
    #     maxn[0] = minn[0] = nums[0]
    #
    #     for i in range(n):
    #         maxn[i] = max(maxn[i - 1] * nums[i], minn[i - 1] * nums[i], nums[i])
    #         minn[i] = min(minn[i - 1] * nums[i], maxn[i - 1] * nums[i], nums[i])
    #
    #     return max(maxn)

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = maxn = minn = nums[0]

        for i in range(1, n):
            mx = maxn
            mn = minn
            maxn = max(mx * nums[i], mn * nums[i], nums[i])
            minn = min(mn * nums[i], mx * nums[i], nums[i])
            ans = max(maxn, ans)

        return ans


arr = [2, 3, -2, 4]
# arr = [-2, 0, -1]
# arr = [-2, 3, -4]
# arr = [2, -5, -2, -4, 3]
print(Solution().maxProduct(arr))
