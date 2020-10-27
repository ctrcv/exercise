from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 方法1：添加一个标记数组
        # 标记数组的方法还可以具有有序性的特点
        ans = []
        n = len(nums)
        used = [False for _ in range(n)]

        def dfs(path):
            if len(path) == n:
                ans.append(path[:])
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(path)
                    used[i] = False
                    path.pop()

        dfs([])
        print(ans)
        return ans

        # 方法2:将数组分为两部分，一部分为已排序过的数据，另一部分为未排序过的数据
        # 如：nums = [1, 2, 3,,4],分为两部分： [1, 2 | 3, 4], 1和2为已经使用过的数据
        # n = len(nums)
        # ans = []
        # def backtrack(first):
        #     if first == n:
        #         ans.append(nums[:])
        #         return
        #     for i in range(first, n):
        #         # 动态维护数组
        #         nums[first], nums[i] = nums[i], nums[first]
        #         # 继续递归填充下一个数
        #         backtrack(first + 1)
        #         # 撤销操作
        #         nums[first], nums[i] = nums[i], nums[first]
        #
        # backtrack(0)
        # print(ans)
        # return ans


inp = [1, 2, 3]
Solution().permute(inp)
