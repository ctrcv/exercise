from typing import List


# 原地标记和修改数组，将数组每个元素值作为索引，将数组对应位置的值乘以-1
# 一遍遍历后，数组中值仍为正的位置即为丢失的元素
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        n = len(nums)
        res = []
        # 第一次遍历。将存在的元素对应的数组中的位置值乘以-1
        for i in range(n):
            idx = abs(nums[i]) - 1
            # 当元素为负值时，说明数组其他位置中已存在当前索引的值
            # 如果再乘以-1的话，会将该位置的元素变正，无法起到标记的作用
            # 所以只对非负数进行乘以-1
            if nums[idx] > 0:
                nums[idx] *= -1

        # 第二次遍历，数组中元素值为正数的索引号即为丢失的值
        for i in range(1, n + 1):
            if nums[i - 1] > 0:
                res.append(i)

        return res


Nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDisappearedNumbers(Nums))
