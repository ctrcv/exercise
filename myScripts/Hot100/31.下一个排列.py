from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        # 从后向前遍历
        # 定义三个指针i，j，k
        i, j, k = n - 2, n - 1, n - 1
        # 1.找到第一个相邻升序的元素（i，j），满足A[i] < A[j]；此时从j到结尾的序列必定为降序的序列
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        # 判断是否为最后一个排列
        if i >= 0:
            # 2.从j到结尾的序列中查找第一个比A[i]大的元素A[k]
            while nums[i] > nums[k]:
                k -= 1
            # 3.交换A[i]和A[k]的值，交换后的从j到结尾的序列此时也必定为降序排列
            nums[i], nums[k] = nums[k], nums[i]
        # 4.对j到结尾序列进行逆置，使其升序排序
        i, j = j, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        # 5.如果在步骤1中找不到符合的相邻元素，则说明原始序列为降序序列，则直接跳到步骤4

        # print(nums)


# Nums = [1,2,3]
# Nums = [3, 2, 1]
Nums = [1, 5, 1]
Solution().nextPermutation(Nums)
