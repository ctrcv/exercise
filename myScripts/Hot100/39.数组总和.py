from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1.回溯法
        # ans = []
        # n = len(candidates)
        #
        # def backtrack(i, val, record):
        #     # 如果差小于0，说明当前元素candidates[i]的值大了
        #     if val < 0:
        #         return
        #     # 等于0，说明方案可行
        #     if val == 0:
        #         ans.append(record[:])
        #         return
        #     for j in range(i, n):
        #         record.append(candidates[j])  # 添加
        #         backtrack(j, val - candidates[j], record)
        #         record.pop()  # 回溯
        #
        # backtrack(0, target, [])
        # return ans

        # 2. 回溯法，剪枝
        # 对candidates进行排序，当差值val<0时，则表示当前位置i之后的元素都不会满足要求
        # 因此跳过进一步的回溯
        # ans = []
        # n = len(candidates)
        # # 排序
        # candidates.sort()
        #
        # def backtrack(i, val, record):
        #     # 如果差小于0，说明当前元素candidates[i]的值大了
        #     if val < 0:
        #         return
        #     # 等于0，说明方案可行
        #     if val == 0:
        #         ans.append(record[:])
        #         return
        #     for j in range(i, n):
        #         if val - candidates[j] < 0:
        #             break
        #         record.append(candidates[j])  # 添加
        #         backtrack(j, val - candidates[j], record)
        #         record.pop()  # 回溯
        #
        # backtrack(0, target, [])
        # return ans

        # 方法1另一种写法,官方提供的不剪枝的朴素回溯法
        # 时间复杂度：O（S），S是所有可行解组成的长度之和，空间复杂度O（target）
        ans = []
        n = len(candidates)

        def backtrack(i, val, record):
            if i == n:
                return
            if val == 0:
                ans.append(record[:])
                return

            # 选择当前数
            if val - candidates[i] >= 0:
                record.append(candidates[i])
                backtrack(i, val - candidates[i], record)
                record.pop()

            # 直接跳过，通过索引后移实现for功能
            backtrack(i + 1, val, record)
        backtrack(0, target, [])
        return ans


# Candidates = [2,3,6,7]
# Target = 7
Candidates = [2, 3, 5]
Target = 8
print(Solution().combinationSum(Candidates, Target))
