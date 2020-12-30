from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 思想，除自身外数组的乘积等于自身元素前的序列之积和自身元素之后的序列之积的乘积
        # 所以可以使用两个数组分别记录位置i的前缀和后缀积，之后将两者相乘即为结果
        n = len(nums)
        # 1.前缀积和后缀积数组记录
        # 前缀积left和right，因题目说明结果数组不算额外空间，所以可用res代替left数组记录前缀积
        # res = [1] * n
        # right = [1] * n
        # # 求位置i的前缀积
        # for i in range(1, n):
        #     res[i] = res[i - 1] * nums[i - 1]
        # # 求位置j的后缀积
        # for j in range(n - 2, -1, -1):
        #     right[j] = right[j + 1] * nums[j + 1]
        # # 前缀积和后缀积相乘，得到除自身外其余元素的积
        # for k in range(n):
        #     res[k] = res[k] * right[k]
        #
        # return res

        # 2.时间和空间优化
        # left前缀积数组因为需要记录，所以该循环和数组必须申请
        # 但right数组没必要再单独申请和循环记录，可以直接与left数组的元素相乘即可
        # right需要后序遍历得到

        # 左前缀数组/结果数组
        res = [1] * n
        # 后缀积指针right
        right = 1
        # 求前缀积，并记录在res中
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        for j in range(n - 2, -1, -1):
            # right 记录右缀积
            right = right * nums[j + 1]
            res[j] = right * res[j]

        return res


Nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(Nums))