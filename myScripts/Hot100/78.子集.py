from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [nums]
        # 方法1：回溯
        # 时间复杂度O(n*2^n).一共2^n个状态，每个状态需要O(n)的时间构建子集
        # 空间复杂度O(n). 临时数组 tt 的空间代价是 O(n)O(n)，递归时栈空间的代价为 O(n)O(n)。
        res = []

        def dfs(curr, t):
            # 记录答案
            if curr == len(nums):
                res.append(t[:])
                return
            # 考虑选择当前位置
            t.append(nums[curr])
            dfs(curr + 1, t)
            t.pop()
            # 不考虑选择当前位置
            dfs(curr + 1, t)

        dfs(0, [])
        return res


Nums = [1, 2, 3]
print(Solution().subsets(Nums))
