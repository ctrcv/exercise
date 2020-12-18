from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 方法1：添加一个标记数组
        # 标记数组的方法还可以具有有序性的特点
        # res = []
        # n = len(nums)
        # used = [False] * n
        #
        # def backtrack(record):
        #     if len(record) == n:
        #         res.append(record[:])
        #         return
        #     for i in range(n):
        #         if not used[i]:
        #             used[i] = True
        #             record.append(nums[i])
        #             backtrack(record)
        #             used[i] = False
        #             record.pop()
        #
        # backtrack([])
        # return res

        # 方法2： 将数组分成两个部分，前半部分是已排列过的数据，后半部分为没有排列过的
        # 如：nums = [1, 2, 3,,4],分为两部分： [1, 2 | 3, 4], 1和2为已经使用过的数据
        res = []
        n = len(nums)

        def backtrack(first):
            if first == n:
                res.append(nums[:])
                return
            for i in range(first, n):
                # 注意：i的初始位置需要从first开始，而不是first + 1
                # 动态维护数组
                # 交换双方位置
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return res


Nums = [1, 2, 3]
print(Solution().permute(Nums))
